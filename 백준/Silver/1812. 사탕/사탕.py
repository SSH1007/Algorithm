import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    result = []
    tmp = 0
    for idx, v in enumerate(lst):
        if idx%2:
            tmp -= v
        else:
            tmp += v
    result.append(tmp//2)
    for i in range(N-1):
        result.append(lst[i]-result[i])
    for i in range(N):
        print(result[i])


if __name__ == '__main__':
    main()