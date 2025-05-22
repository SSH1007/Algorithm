import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = []
    for n in range(1, N+1):
        tmp = [n]+list(map(int, input().split()))
        lst.append(tmp)
    lst.sort(key=lambda x: (-x[1], x[2], x[3]))
    print(lst[0][0])


if __name__ == '__main__':
    main()