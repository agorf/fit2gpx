#!/usr/bin/env python

import sys
from os import path
from time import sleep

from .fit_converter import FitConverter

def main():
    if len(sys.argv) < 2:
        print("Usage: fit2gpx <file1.fit> [file2.fit ...]")
        sys.exit(1)

    for fit_path in sys.argv[1:]:
        print(f"{fit_path} -> ", end='')

        if not path.isfile(fit_path):
            print("file not found")
            continue

        try:
            gpx_path = FitConverter(fit_path).convert()
            print(gpx_path if gpx_path else "no data")
        except Exception:
            print("conversion failed")

        sleep(1) # Max 1 req/sec

if __name__ == "__main__":
    main()
