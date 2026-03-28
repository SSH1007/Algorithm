import sys
input = lambda: sys.stdin.readline().rstrip()
import math


def main():
    w, h = map(int, input().split())
    r = int(input())
    pi = math.pi
    print(w*h-r*r*pi/4)


if __name__ == '__main__':
    main()