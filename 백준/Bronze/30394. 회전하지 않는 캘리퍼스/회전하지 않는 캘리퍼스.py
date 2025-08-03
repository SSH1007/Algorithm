import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    maxY, minY = -float('inf'), float('inf')
    for _ in range(N):
        x, y = map(int, input().split())
        maxY = y if y > maxY else maxY
        minY = y if y < minY else minY
    print(maxY-minY)


if __name__ == '__main__':
    main()