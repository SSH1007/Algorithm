import sys
input = lambda: sys.stdin.readline().rstrip()


def F(i):
    if i//10000 < 24 and i%100 < 60 and (i%10000)//100 < 60:
        return True
    return False


def main():
    T = 235960
    for _ in range(3):
        a, b = input().split()
        A = int(''.join(a.split(':')))
        B = int(''.join(b.split(':')))
        dap = 0
        if A > B:
            for i in range(A, T):
                if i%3 == 0 and F(i):
                    dap += 1
            for i in range(B+1):
                if i%3 == 0 and F(i):
                    dap += 1
        else:
            for i in range(A, B+1):
                if i%3 == 0 and F(i):
                    dap += 1
        print(dap)


if __name__ == '__main__':
    main()