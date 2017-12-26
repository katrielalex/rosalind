#!/usr/bin/env python3

import argparse
import sys


def fib(n, k):
    pairs = 1
    for i in range(n):
        pairs += k * pairs
    return pairs


def main(args):
    s = args.seq
    print(fib(s))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n")
    parser.add_argument("k")
    args = parser.parse_args()

    sys.exit(main(args))
