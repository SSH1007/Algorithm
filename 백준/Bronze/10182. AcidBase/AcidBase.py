import sys
input = lambda: sys.stdin.readline().rstrip()
import math


def main():
    N = int(input())
    for _ in range(N):
        a, b = input().split(' = ')
        c = math.log10(float(b))
        if a == 'H':
            d = -c
        else:
            d = 14+c
        print(f'{d:.2f}')


if __name__ == '__main__':
    main()