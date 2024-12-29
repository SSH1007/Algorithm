import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    rooms = [i for i in range(1, N+1)]
    M = int(input())
    lst = []
    for _ in range(M):
        x, y = map(int, input().split())
        lst.append((x, y))
    lst.sort()
    for x, y in lst:
        for i in range(x, y):
            rooms[i] = rooms[i-1]
    print(len(set(rooms)))


if __name__ == '__main__':
    main()