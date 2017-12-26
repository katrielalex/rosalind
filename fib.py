#!/usr/bin/env python3

import argparse
import sys


def fib(n, k):
    pairs = 1
    infants = 0
    for i in range(n-1):
        pairs, infants = pairs + infants, k * pairs
    return pairs


def main(args):
    print(fib(args.n, args.k))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("k", type=int)
    args = parser.parse_args()

    sys.exit(main(args))
