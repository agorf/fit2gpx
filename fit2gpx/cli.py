#!/usr/bin/env python

import sys
from time import sleep

from .fit_converter import FitConverter

def main():
    if len(sys.argv) < 2:
        print("Usage: fit2gpx <file1.fit> [file2.fit ...]")
        sys.exit(1)

    for fit_path in sys.argv[1:]:
        FitConverter(fit_path).convert()
        sleep(1) # Max 1 req/sec

if __name__ == "__main__":
    main()
