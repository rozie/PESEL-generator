#/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import calendar

days_month_count = {
    1: 31,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

multipliers = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]


def pesel_checksum(pesel):
    sum = 0
    pesel_list = map(int, list(pesel))
    for a, b in zip(pesel_list, multipliers):
        sum += a * b
    checksum = (10 - sum % 10) % 10
    return checksum


def main():
    args = parse_arguments()
    start = args.start_year
    end = args.end_year
    if end < start:
        start = args.end_year
        end = args.start_year
    if start < 1900:
        print("Years over 1900 are supported")
        exit()
    for year in range(start, end+1):
        year_last = year % 100
        for month in range(1, 12+1):
            if month == 2:
                if calendar.isleap(year):
                    days_count = 29
                else:
                    days_count = 28
            else:
                days_count = days_month_count.get(month, 31)
            if year > 1999:
                month += 20
            for day in range(1, days_count+1):
                for number in range(0, 10000):
                    pesel = str(year_last * 100000000 + month * 1000000 + day * 10000 + number).zfill(10)
                    checksum = pesel_checksum(pesel)
                    pesel += str(checksum)
                    print(pesel)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='PESEL number generator')
    parser.add_argument(
        '-s', '--start-year', required=False,
        default=1940, type=int,
        help="Minimum year to generate PESEL numbers")
    parser.add_argument(
        '-e', '--end-year', required=False,
        default=1999, type=int,
        help="Maximum year to generate PESEL numbers")
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    main()
