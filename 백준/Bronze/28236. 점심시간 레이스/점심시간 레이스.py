import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m, k = map(int, input().split())
    lst = []
    for c in range(1, k+1):
        f, d = map(int, input().split())
        lst.append((c, abs(f-1)+abs(d-m)))
    lst.sort(key=lambda x: x[1])
    print(lst[0][0])


if __name__ == '__main__':
    main()