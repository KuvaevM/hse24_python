#!/usr/bin/env python3
import os
import sys


def tail(files=None):
    if files:
        for file in files:
            print(f"==> {file} <==")
            if not os.path.exists(file):
                print(f"Error: File '{file}' not found.")
            else:
                with open(file, 'r') as f:
                    lines = f.readlines()
                    last_lines = lines[-10:]
                    for line in last_lines:
                        print(line, end='')
                    print()
    else:
        lines = sys.stdin.readlines()
        last_lines = lines[-17:]
        for line in last_lines:
            print(line, end='')





if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail(sys.argv[1:])
    else:
        tail()
