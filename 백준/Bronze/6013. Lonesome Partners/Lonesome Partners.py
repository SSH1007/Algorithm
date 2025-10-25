import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = []
    for _ in range(N):
        x, y = map(int, input().split())
        lst.append((x, y))
    M = 0
    a, b = 0, 0
    for i in range(N):
        for j in range(i+1, N):
            m = ((lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2)**0.5
            if M < m:
                M = m
                a, b = i, j
    print(a+1, b+1)


if __name__ == '__main__':
    main()