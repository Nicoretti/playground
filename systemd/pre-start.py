# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import sys

def main() -> None:
    print("Hello from pre-start.py! (stdout)")
    print("Hello from pre-start.py! (stderr)", file=sys.stderr)


if __name__ == "__main__":
    main()
