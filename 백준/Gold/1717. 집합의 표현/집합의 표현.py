import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def merge(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        parent[y] = x

    def isUnion(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return True
        return False

    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            merge(a, b)
        else:
            if isUnion(a, b):
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()