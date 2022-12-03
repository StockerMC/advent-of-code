if __name__ == '__main__':
    import argparse
    import functools
    import importlib
    import util

    parser = argparse.ArgumentParser()
    parser.add_argument('year', type=int)
    parser.add_argument('day', type=int)
    # parser.add_argument('part', type=int)
    args = parser.parse_args()
    year = args.year
    day = args.day
    # part = args.part

    module = importlib.import_module(f'{year}.day_{day}')
    for part in ('one', 'two'):
        func = getattr(module, f'part_{part}')
        func()
