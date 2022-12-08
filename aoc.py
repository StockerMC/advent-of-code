# Runner regex/sample code inspired by https://github.com/LyricLy/aoc/blob/master/runner/main.py

from __future__ import annotations

import argparse
import collections
import datetime
import importlib.util
import pathlib
import re
import time
from zoneinfo import ZoneInfo

import requests

REGEX_FLAGS = re.DOTALL
SAMPLE_INPUT_REGEX = r'For example.*?:.*?<pre><code>(.*?)</code></pre>'
SAMPLE_P1_ANSWER_REGEX = r'.*?<code><em>(.*?)</em></code>'
SAMPLE_P2_ANSWER_REGEX = r'Part Two.*?<code><em>(.*?)</em></code>'
TIME_REGEX = r'You have (?:(\d+)m)?(\d+)s left to wait.'

def i(s: str):
    return int(s) if s.isdigit() else s

class Runner:
    def __init__(self, year: int, day: int, override_samples: bool) -> None:
        self.session = session = requests.Session()
        session.headers.update({
            'User-Agent': 'https://github.com/StockerMC/advent-of-code',
            'Cookie': f'session={self.get_session_cookie()}',
        })
        self.year = year
        self.day = day
        self.url = f'https://adventofcode.com/{year}/day/{day}'
        self.bad_attempts: dict[int, list[int | str]] = collections.defaultdict(list)
        self.override_samples = override_samples

    def get_sample(self, part: int) -> tuple[str, str | int] | None:
        path = pathlib.Path(__file__).parent / f'{self.year}/inputs/day_{self.day}_p{part}.txt'
        if path.exists() and not self.override_samples:
            text = path.read_text()
            sample_input, sample_answer = text.split('::|::')
            return sample_input.strip('\n'), i(sample_answer.strip('\n'))

        print('Fetching sample input...')
        response = self.session.get(f'https://adventofcode.com/{self.year}/day/{self.day}')
        response.raise_for_status()

        html = response.text
        # doesn't work for all < 2022 days, may need to use findall for that instead
        if not (match := re.search(SAMPLE_INPUT_REGEX, html, REGEX_FLAGS)):
            return None

        sample_input = match.group(1)

        regex = SAMPLE_P1_ANSWER_REGEX if part == 1 else SAMPLE_P2_ANSWER_REGEX
        if not (match := re.search(regex, html, REGEX_FLAGS)):
            return None

        sample_answer = match.group(1)
        with open(path, 'w') as f:
            f.write(f'{sample_input}::|::\n{sample_answer}')

        return sample_input.strip('\n'), i(sample_answer.strip('\n'))

    @staticmethod
    def get_session_cookie():
        with open(pathlib.Path(__file__).parent / 'SESSION') as f:
            return f.read().strip()

    def get_input(self) -> str:
        path = pathlib.Path(__file__).parent / f'{self.year}/inputs/day_{self.day}.txt'
        if path.exists():
            return path.read_text()

        response = self.session.get(f'{self.url}/input')
        response.raise_for_status()

        text = response.text.rstrip('\n')
        path.write_text(text)
        return text

    # TODO: validate type of submission

    def get_module(self):
        name = f'day_{self.day}'
        path = pathlib.Path(__file__).parent / f'{self.year}/{name}.py'
        spec = importlib.util.spec_from_file_location(name, path)
        if spec is None:
            raise Exception(f'Cannot find {path}')

        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)  # type: ignore
        except Exception as e:
            raise Exception(f'Cannot compile {name}') from e

        return module

    def call_part(self, part: int, lines: str):
        module = self.get_module()
        func = getattr(module, f'part_{"one" if part == 1 else "two"}')
        return func(lines.splitlines())

    @staticmethod
    def confirm(msg: str, default: bool = True) -> bool:
        cont = input(msg).lower()
        return default if cont == '' else cont == 'y'

    def verify_sample(self, part: int) -> bool:
        print(f'Verifying the part {part} solution with the sample input...')
        sample = self.get_sample(part)
        if sample is None:
            return self.confirm(f"Can't verify the solution with the sample input. Submit anyways (Y/n)?")

        inp, ans = sample
        ret = self.call_part(part, inp)
        if ret is None:
            print('Return value is None; not submitting.')
            return False
        elif not isinstance(ret, type(ans)):
            print(f'Return type is {type(ret).__name__}; should be {type(ans).__name__} ({ans!r}).')
            # When the sample wasn't parsed correctly (older years)
            cont = self.confirm('Do you want to manually enter the sample input (y/N)?', default=False)
            if cont:
                print('Enter the input ("input"::|::"answer"<newline>::|::) (without the quotes):')
                lines = [line for line in iter(input, '::|::')]
                with open(pathlib.Path(__file__).parent / f'{self.year}/inputs/day_{self.day}_p{part}.txt', 'w') as f:
                    f.write('\n'.join(lines))
                return self.verify_sample(part)
                    
            return False
        elif ans != ret:
            msg = f'Return value is {ret!r}; should be {ans!r}.'
            if isinstance(ans, int):
                msg += f' Return value is {abs(ret - ans)} off.'  # type: ignore
            print(msg)
            return False

        return True

    def solve(self, part: int):
        from typing import TYPE_CHECKING
        if not TYPE_CHECKING:
            module = self.get_module()
            for part in ('one', 'two'):
                func = getattr(module, f'part_{part}')
                ret = func()
                print(f'Part {part}: {ret}')
        if TYPE_CHECKING:
            for p in range(part, 3):
                # verified = self.verify_sample(p)
                # if not verified:
                #     return
                # inp = self.get_input()
                # ret = self.call_part(p, inp)
                # self.submit(p, ret)
                ...

    def sleep(self, seconds: int, part: int, answer: int | str):
        padding = len(str(seconds))
        for s in range(seconds, 0, -1):
            print('Remaining: {s:0{padding}}s'.format(s=s, padding=padding), end='\r')
            time.sleep(1)

        cont = False
        while not cont:
            cont = self.confirm(f'Ready to submit part {part} (Y/n)?')
            if cont:
                return self.submit(part)

    def submit(self, part: int):
        verified = self.verify_sample(part)
        if not verified:
            return False

        inp = self.get_input()
        answer = self.call_part(part, inp)

        bad_attempts = self.bad_attempts[part]
        if answer in bad_attempts:
            print(f'Already tried submitting this answer: {answer}')
            cont = self.confirm('Try again (Y/n)?')
            if cont:
                self.submit(part)

        response = self.session.post(f'{self.url}/answer', data={'level': part, 'answer': answer})
        text = response.text
        if "That's the right answer" in text:
            print('Correct!')
            if part == 1:
                self.bad_attempts[2].append(answer)
                return self.confirm('Move on to part 2 (Y/n)?')
            else:
                print('Finished!')
                return False

        elif "That's not the right answer" in text:
            print(f'Incorrect answer: {answer}. Sleeping 60 seconds.')
            self.bad_attempts[part].append(answer)
            return self.sleep(60, part, answer)

        elif 'You gave an answer too recently' in text:
            print('You have to wait before submitting.')
            if (match := re.search(text, TIME_REGEX)):
                m, s = match.groups()
                m = int(m) if m else 0
                s = int(s) + m
            else:
                print('Cannot find remaining time.')
                s = 0

            return self.sleep(s, part, answer)

        elif 'Did you already complete it' in text:
            print("You've already completed this part.")

def get_date() -> tuple[int, int]:
    now = datetime.datetime.now(ZoneInfo("America/New_York"))
    if now.month == 12:
        year = now.year
    else:
        year = now.year - 1

    return year, now.day

def main():
    year, day = get_date()
    parser = argparse.ArgumentParser()
    parser.add_argument('--year', '-y', type=int, default=year)
    parser.add_argument('--day', '-d', type=int, default=day)
    parser.add_argument('--part', '-p', type=int, default=1)
    parser.add_argument('--override-samples', '-os', action='store_true')
    args = parser.parse_args()
    runner = Runner(args.year, args.day, override_samples=args.override_samples)
    cont = runner.submit(args.part)
    if cont:
        runner.submit(args.part + 1)

if __name__ == '__main__':
    main()

# TODO: interactive session with submit/verify commands
# TODO: ALLOW TO RUN FILE BEFORE SUBMITTING