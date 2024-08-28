import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    info = []
    for _ in range(N):
        a, b = input().split()
        b = int(b)
        info.append((a, b))
    for _ in range(M):
        power = int(input())
        s, e = 0, N-1
        while s <= e:
            mid = (s+e)//2
            if power > info[mid][1]:
                s = mid+1
            else:
                e = mid-1
        print(info[s][0])


if __name__ == '__main__':
    main()