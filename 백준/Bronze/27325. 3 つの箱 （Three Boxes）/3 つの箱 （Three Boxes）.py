import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    cur, cnt = 1, 0
    for s in S:
        if s == 'L':
            cur = max(cur-1, 1)
        else:
            cur = min(cur+1, 3)
        if cur == 3:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()