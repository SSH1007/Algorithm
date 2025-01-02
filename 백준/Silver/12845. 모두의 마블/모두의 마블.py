import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    print(sum(lst[:N-1])+lst[-1]*(N-1))


if __name__ == '__main__':
    main()