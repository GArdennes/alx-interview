#!/usr/bin/python3
"""
Stats script
"""

import sys


def main():
    """
    Script to read stdin line by line and compute metrics
    """
    total_size = 0
    status_count = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            ip, _, _, _, _, _, _, s_cde, fl_s = line.rstrip(
                    ).split()
            fl_s = int(fl_s)
            total_size += fl_s

            if s_cde.isdigit():
                s_cde = int(s_cde)
                status_count[s_cde] = status_count.get(
                        s_cde, 0
                        ) + 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_count)
                status_count.clear()

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)


def print_statistics(total_size, status_count):
    """
    Method that prints the statistics
    """
    print(f"File size: {total_size}")
    for key, value in sorted(status_count.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
