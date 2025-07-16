import sys
input = lambda: sys.stdin.readline().rstrip()


def F(x):
    x /= 10
    if int((x%1)*10) > 4:
        return int(x)+1
    else:
        return int(x)


def main():
    z = int(input())
    for _ in range(z):
        R, G, B = 0, 0, 0
        for _ in range(10):
            r, g, b = map(int, input().split())
            R += r
            G += g
            B += b
        print(F(R), F(G), F(B))


if __name__ == '__main__':
    main()