import sys
input = lambda: sys.stdin.readline().rstrip()
import itertools


def main():
    lst = list(map(int, input().split()))
    n = int(input())
    print(sorted([int(''.join(map(str, l))) for l in list(itertools.permutations(lst, 3))]).index(n)+1)


if __name__ == '__main__':
    main()