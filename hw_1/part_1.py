#!/usr/bin/env python3
import os
import sys


def nl(file=None):
    if file:
        if not os.path.exists(file):
            print(f"Error: File '{file}' not found.")
            sys.exit(1)
        with open(file, 'r') as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    for i, line in enumerate(lines):
        print(f"{i + 1}\t{line}", end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()
