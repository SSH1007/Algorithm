import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    F, C, E, B = map(int, input().split())
    oF, oC, oE, oB = map(int, input().split())
    Q = int(input())
    cookie = 0
    for _ in range(Q):
        q, i = map(int, input().split())
        if q == 1:
            if oF*i <= F and oC*i <= C and oE*i <= E and oB*i <= B:
                F -= oF*i
                C -= oC*i
                E -= oE*i
                B -= oB*i
                cookie += i
                print(cookie)
            else:
                print('Hello, siumii')
        elif q == 2:
            F += i
            print(F)
        elif q == 3:
            C += i
            print(C)
        elif q == 4:
            E += i
            print(E)
        else:
            B += i
            print(B)


if __name__ == '__main__':
    main()