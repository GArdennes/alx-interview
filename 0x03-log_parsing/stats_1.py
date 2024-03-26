#!/usr/bin/env python3
import sys
from collections import defaultdict


def parse_line(line):
  """Parses a line and returns a dictionary with extracted data."""
  try:
    # Split the line with spaces as delimiters
    parts = line.split()
    ip, _, _, path, http_version, status_code, file_size = parts
    return {
        "ip": ip,
        "status_code": int(status_code),
        "file_size": int(file_size)
    }
  except (ValueError, IndexError):
    # Ignore lines with parsing errors
    return None

def print_stats(total_size, status_counts):
  """Prints statistics for total size and status code counts."""
  print(f"File size: {total_size}")
  for code, count in sorted(status_counts.items()):
    print(f"{code}: {count}")

try:
  total_size = 0
  status_counts = defaultdict(int)
  line_count = 0

  for line in iter(sys.stdin.readline, ''):
    line_count += 1
    data = parse_line(line.rstrip())

    # Skip lines with parsing errors
    if not data:
      continue

    total_size += data["file_size"]
    status_counts[data["status_code"]] += 1

    # Print stats after every 10 lines or on keyboard interrupt
    if line_count % 10 == 0 or line_count == 1:
      print_stats(total_size, status_counts)
      status_counts.clear()  # Reset counts for the next interval

except KeyboardInterrupt:
  print("\n-- Interrupted --")
  print_stats(total_size, status_counts)
