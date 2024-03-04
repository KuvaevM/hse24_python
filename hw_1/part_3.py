#!/usr/bin/env python3
import os
import sys


def wc(files=None):
    total_lines = 0
    total_words = 0
    total_chars = 0

    if files:
        for file in files:
            lines = 0
            words = 0
            chars = 0

            if not os.path.exists(file):
                print(f"Error: File '{file}' not found.")
            else:
                with open(file, 'r') as f:
                    data = f.readlines()
                    lines = ''.join(data).count('\n')
                    for line in data:
                        words += len(line.split())
                        chars += len(line)

                total_lines += lines
                total_words += words
                total_chars += chars

                print(f"{lines} {words} {chars} {file}")
        print(f"{total_lines} {total_words} {total_chars} total")

    else:
        data = sys.stdin.read()
        lines = data.count('\n')
        words = len(data.split())
        chars = len(data)

        print(f"\t{lines}\t{words}\t{chars}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        wc()
