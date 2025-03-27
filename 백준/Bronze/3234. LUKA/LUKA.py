import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X, Y = map(int, input().split())
    K = int(input())
    S = input()
    lst = []
    x, y = 0, 0
    if abs(X-x) <= 1 and abs(Y-y) <= 1:
        lst.append(0)
    for k in range(K):
        if S[k] == 'I':
            x += 1
        elif S[k] == 'S':
            y += 1
        elif S[k] == 'Z':
            x -= 1
        else:
            y -= 1
        if abs(X - x) <= 1 and abs(Y - y) <= 1:
            lst.append(k+1)
    if len(lst) == 0:
        print(-1)
    else:
        for l in lst:
            print(l)


if __name__ == '__main__':
    main()