import sys
input = lambda: sys.stdin.readline().rstrip()
import re


def main():
    pattern = re.compile('(100+1+|01)+$')
    T = int(input())
    for _ in range(T):
        st = input()
        if pattern.match(st):
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    main()