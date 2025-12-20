import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, P, Q = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    lst = []
    for n in range(N):
        i = 0
        while i != 10000:
            if As[n] == Bs[n]:
                break
            As[n] += P
            Bs[n] += Q
            i += 1
        if i == 10000:
            print('NO')
            return
        else:
            lst.append(i)
    print('YES')
    print(*lst)


if __name__ == '__main__':
    main()