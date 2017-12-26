#!/usr/bin/env python3

import argparse
import sys


def main(args):
    s = args.seq
    bases = "ACGT"
    print(" ".join(str(s.count(base)) for base in bases))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seq")
    args = parser.parse_args()

    sys.exit(main(args))
