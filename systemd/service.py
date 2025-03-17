#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
# ]
# ///

import sys
import time

def main() -> None:
    while True:
        print("Hello from service.py! (stdout)")
        print("Hello from service.py! (stderr)", file=sys.stderr)
        time.sleep(1)


if __name__ == "__main__":
    main()
