#!/usr/bin/env python3
"""
Stats script
"""

import sys
from typing import Dict


def main():
    """
    Script to read stdin line by line and compute metrics
    """
    total_size = 0
    status_count = {}

    try:
        for line in sys.stdin:
            try:
                ip, _, _, _, status_code, file_size = line.split()
                file_size = int(file_size)
                total_size += file_size

                if status_code.isdigit():
                    status_code = int(status_code)
                    status_count[status_code] = status_count.get(
                            status_code, 0
                            ) + 1

                if len(status_count) == 10:
                    print_statistics(total_size, status_count)
                    status_count.clear()

            except ValueError:
                continue

    except KeyboardInterrupt:
        print_statistics(total_size, status_count)


def print_statistics(total_size: int, status_count: Dict[int, int]) -> None:
    """
    Method that prints the statistics
    """
    print(f"File size: {total_size}")
    for key, value in sorted(status_count.items()):
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
