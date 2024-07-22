import sys
input = lambda: sys.stdin.readline().rstrip()
import re


def main():
    sound = input()
    # |는 or, +는 1개 이상 반복
    # 문자열이 (100+1+|01)+로 끝나면 OK
    pattern = re.compile('(100+1+|01)+$')

    if pattern.match(sound):
        print('SUBMARINE')
    else:
        print('NOISE')


if __name__ == '__main__':
    main()