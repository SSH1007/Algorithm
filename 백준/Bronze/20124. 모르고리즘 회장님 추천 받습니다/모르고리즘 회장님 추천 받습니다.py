import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = []
    for _ in range(N):
        n, s = input().split()
        lst.append((n, int(s)))
    lst.sort(key=lambda x: (-x[1], x[0]))
    print(lst[0][0])


if __name__ == '__main__':
    main()