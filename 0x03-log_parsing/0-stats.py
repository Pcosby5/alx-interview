#!/usr/bin/python3
"""
Log parsing
"""

import sys


if __name__ == '__main__':

    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Print the statistics of the log file.

        Args:
            stats (dict): A dictionary containing the statistics of
            the log file
            where the key is the HTTP status code and the value is the
            count of the status code
            file_size (int): The size of the log file

        Returns:
            None
        """
        print("File size: {:d}".format(file_size))
        # Sort the statistics by HTTP status code
        for k, v in sorted(stats.items()):
            # Only print the status code and count if the count is not zero
            if v:
                print("{}: {}".format(k, v))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except BaseException:
                pass
            try:
                filesize += int(data[-1])
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats(stats, filesize)
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print_stats(stats, filesize)
        raise
