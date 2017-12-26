#!/usr/bin/env python3

import argparse
import sys


def revc(seq):
    # first T <-> A
    seq = seq.replace("T", "_").replace("A", "T").replace("_", "A")

    #  then C <-> G
    seq = seq.replace("C", "_").replace("G", "C").replace("_", "G")

    # then reverse
    return seq[::-1]


def main(args):
    s = args.seq
    print(revc(s))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seq")
    args = parser.parse_args()

    sys.exit(main(args))
