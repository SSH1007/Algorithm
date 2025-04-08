import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    buckets = [0]*1001
    for n in range(1, N+1):
        s, t, b = map(int, input().split())
        for i in range(s, t+1):
            buckets[i] += b
    print(max(buckets))


if __name__ == '__main__':
    main()