import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def main():
    N = int(input())
    island = [i for i in range(N+1)]

    def find(x):
        if island[x] == x:
            return x
        island[x] = find(island[x])
        return island[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        island[y] = x

    def isUnion(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return True
        return False

    for _ in range(N-2):
        a, b = map(int, input().split())
        union(a, b)
    for i in range(1, N):
        for j in range(i+1, N+1):
            if not isUnion(i, j):
                print(i, j)
                exit(0)


if __name__ == '__main__':
    main()