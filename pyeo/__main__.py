#!/usr/bin/env python
import sys


def main():
    try:
        print('Hello, PyEO!')
        exit_status = 0
    except KeyboardInterrupt:
        exit_status = -1
    sys.exit(exit_status)


if __name__ == '__main__':
    main()
