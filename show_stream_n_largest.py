#!/usr/bin/python3 -u
import heapq
import sys
import termios
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Displays top limit values',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-l', '--limit', type=int, default=4, help='max lines to be printed')
    args = parser.parse_args()
    limit = args.limit
    h = []
    for i, line in enumerate(sys.stdin, 1):
        line = int(line.strip())
        func = heapq.heappush if i <= limit else heapq.heappushpop
        func(h, line)
        print("\x1b[2J\x1b[H")
        print(*heapq.nlargest(limit, h), sep='\n')
