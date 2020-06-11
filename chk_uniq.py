#!/usr/bin/env python
"""This script reports equal datasets

Typical usage:

    ./chk_uniq.py all.json > chk_uniq.txt

"""

from sys import argv
from json import load


def main():
    try:
        in_file = argv[1]
    except IndexError:
        in_file = 'all.json'

    with open(in_file) as f:
        db = load(f)

    last_data = None
    out_lines = []
    current_line = ''
    for src_name in sorted(db.keys()):
        if last_data != db[src_name]['data'] and current_line != '':
            out_lines.append(current_line[:-1])
            current_line = ''
        last_data = db[src_name]['data']
        current_line += (src_name + ' ')

    print('#\n# Each line contains names of equal datasetes\n#')
    print('\n'.join(out_lines))


if __name__ == '__main__':
    main()
