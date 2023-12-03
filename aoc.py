# Runner regex/sample code inspired by https://github.com/LyricLy/aoc/blob/master/runner/main.py

from __future__ import annotations

import argparse
import collections
import datetime
from html import unescape
import importlib.util
import pathlib
import re
import time
from zoneinfo import ZoneInfo

import requests

REGEX_FLAGS = re.DOTALL
SAMPLE_P1_INPUT_REGEX = r'For example.*?:.*?<pre><code>(.*?)</code></pre>'
SAMPLE_P2_INPUT_REGEX = r'Part Two.*?For example.*?:.*?<pre><code>(.*?)</code></pre>'
SAMPLE_P1_ANSWER_REGEX = r'.*?<code><em>(.*?)</em></code>'
SAMPLE_P2_ANSWER_REGEX = r'Part Two.*?<code><em>(.*?)</em></code>'
TIME_REGEX = r'You have (?:(\d+)m )?(\d+)s left to wait.'

def i(s: str):
    try:
        return int(s)
    except ValueError:
        return s

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

        html = unescape(response.text)
        regex = SAMPLE_P1_INPUT_REGEX if part == 1 else SAMPLE_P2_INPUT_REGEX
        if not (match := re.search(regex, html, REGEX_FLAGS)):
            return None

        sample_input = match.group(1)

        # TODO: doesn't work for all inputs, use findall[-1] and change regex to stop before part two
        regex = SAMPLE_P1_ANSWER_REGEX if part == 1 else SAMPLE_P2_ANSWER_REGEX
        # breakpoint()
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

        text = unescape(response.text)
        if not text.endswith('\n'):
            text += '\n'
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
        converter = getattr(func, 'converter', None)
        param = lines.splitlines()
        if converter is not None:
            param = [converter(line) for line in param]
        return func(param)

    # @staticmethod
    # def confirm(msg: str, debug_option: bool = False) -> bool:
    #     cont = input(f'{msg} ').lower()
    #     return default if cont == '' and default is not None else cont == 'y'

    def write_sample(self, part: int, lines: list[str], answer: int | str) -> None:
        path = pathlib.Path(__file__).parent / f'{self.year}/inputs/day_{self.day}_p{part}.txt'
        with open(path, 'w') as f:
            f.write('\n'.join(lines) + f'\n::|::\n{answer}')

    def confirm(self, msg: str, *, extra: list[str] | None = None) -> str:
        cont = None
        opts = ['', 'y']
        if extra:
            opts.extend(extra)

        while cont not in opts:
            cont = input(f'{msg} ').lower()
        return 'y' if cont == '' else cont

    def manual_input(self, part: int):
        lines = answer = None
        if part == 2:
            # TODO: fix infinite "verifying the part ... solution" loop
            cont = self.confirm('Do you want to use the sample input for part 1 (Y/n)?', extra=['n'])
            if cont == 'y':
                part_one_sample = self.get_sample(part - 1)
                if part_one_sample is None:
                    print('Cannot parse the sample input for part 1.')
                else:
                    # TODO: automatically get the sample answer for part 2
                    lines = part_one_sample[0].splitlines()
                    answer = input('Enter the answer: ')

        if lines is None or answer is None:
            cont = self.confirm('Do you want to manually enter the sample input? (Y/n)', extra=['n'])
            if cont == 'n':
                return False

            print('Enter the input (EOF indicated by ::|:: on a new line):')
            lines = [line for line in iter(input, '::|::')]
            answer = input('Enter the answer: ')

        self.write_sample(part, lines, answer)
        return self.verify_sample(part)

    def verify_sample(self, part: int) -> bool:
        print(f'Verifying the part {part} solution with the sample input...')
        sample = self.get_sample(part)
        if sample is None:
            # When the sample wasn't parsed correctly
            print('Cannot parse the sample input.')
            return self.manual_input(part)

        inp, ans = sample
        ret = self.call_part(part, inp)
        if ret is None:
            print('Return value is None; not submitting.')
            return False
        elif not isinstance(ret, type(ans)):
            print(f'Return type is {type(ret).__name__}; should be {type(ans).__name__} ({ans!r}).')
            # When the sample wasn't parsed correctly (older years)
            return self.manual_input(part)
        elif ans != ret:
            msg = f'Return value is {ret!r}; should be {ans!r}.'
            if isinstance(ans, int):
                msg += f' Return value is {abs(ret - ans)} off.'  # type: ignore
            print(msg)
            return False

        print(f'Sample answer is correct: {ans}')
        return True

    def sleep(self, seconds: int, part: int, answer: int | str) -> None:
        padding = len(str(seconds))
        for s in range(seconds, 0, -1):
            print('Remaining: {s:0{padding}}s'.format(s=s, padding=padding), end='\r')
            time.sleep(1)

        self.confirm(f'Ready to submit part {part} (Y)?')
        return self.submit(part)

    def submit(self, part: int) -> None:
        verified = self.verify_sample(part)
        if not verified:
            opt = self.confirm('Try verifying with the sample again (Y/n)?', extra=['n'])
            if opt == 'y':
                return self.submit(part)

        opt = self.confirm(f'Ready to submit part {part} (y/d)?', extra=['d'])
        if opt == 'd':
            return self.submit(part)

        inp = self.get_input()
        answer = self.call_part(part, inp)

        bad_attempts = self.bad_attempts[part]
        if answer in bad_attempts:
            print(f'Already tried submitting this answer: {answer}')
            self.confirm('Try again (Y)?')
            return self.submit(part)

        response = self.session.post(f'{self.url}/answer', data={'level': part, 'answer': answer})
        response.raise_for_status()
        text = response.text
        if "That's the right answer" in text:
            print('Correct!')
            if part == 1:
                self.bad_attempts[2].append(answer)
                print('Moving on to part 2.')
                self.submit(part + 1)
            else:
                print('Finished!')

        elif "That's not the right answer" in text:
            print(f'Incorrect answer: {answer}. Sleeping 60 seconds.')
            self.bad_attempts[part].append(answer)
            return self.sleep(60, part, answer)

        elif 'You gave an answer too recently' in text:
            print('You have to wait before submitting.')
            if (match := re.search(TIME_REGEX, text)):
                m, s = match.groups()
                m = int(m) if m else 0
                s = int(s) + m
            else:
                print('Cannot find remaining time.')
                s = 0

            return self.sleep(s, part, answer)

        elif 'Did you already complete it' in text:
            print("You've already completed this part.")
            if part == 1:
                return self.submit(part + 1)

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
    runner.submit(args.part)

if __name__ == '__main__':
    main()

# TODO: interactive session with submit/verify commands
# TODO: ALLOW TO RUN FILE BEFORE SUBMITTING (TO TEST)
# TODO: use part 1 input if cant find part 2