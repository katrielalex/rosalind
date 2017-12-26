#!/usr/bin/env python3

import argparse
import sys


def main(args):
    s = args.seq
    print(s.replace("T", "U"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("seq")
    args = parser.parse_args()

    sys.exit(main(args))
