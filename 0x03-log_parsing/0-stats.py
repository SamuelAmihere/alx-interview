#!/usr/bin/python3
"""
Log Parsing:
"""

import sys


def print_stats(file_size, status_codes):
    """
    Prints the file size and status codes
    """
    print("File size: {}".format(file_size), flush=True)
    for key in sorted(status_codes.keys()):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]), flush=True)


def check_line(line):
    """
    Checks the line format using regex
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
        <status code> <file size>
    """
    import re
    pattern = r"(\d+\.\d+\.\d+\.\d+) - \[(\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\] "\
              r"\"[^\"]*\" (\d+) (\d+)"
    match = re.match(pattern, line)
    if match:
        return match.groups(), True
    else:
        return None, False


def main():
    """
    Main function
    """
    file_size = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            data, right_format = check_line(line)
            if not right_format:
                continue
            if len(data) > 2:
                file_size += int(data[-1])
                if data[-2] in status_codes:
                    status_codes[data[-2]] += 1
            if count == 10:
                print_stats(file_size, status_codes)
                count = 0
    except (KeyboardInterrupt, EOFError):
        print_stats(file_size, status_codes)
        raise

    print_stats(file_size, status_codes)


if __name__ == "__main__":
    main()
