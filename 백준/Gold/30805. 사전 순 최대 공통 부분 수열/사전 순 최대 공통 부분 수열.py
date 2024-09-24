import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    A = list(map(int, input().split()))
    _= int(input())
    B = list(map(int, input().split()))

    def F(A, B, lst):
        if not A or not B:
            return lst

        Amax, Bmax = max(A), max(B)
        AmaxIdx, BmaxIdx = A.index(Amax), B.index(Bmax)

        if Amax == Bmax:
            lst.append(Amax)
            return F(A[AmaxIdx+1:], B[BmaxIdx+1:], lst)
        else:
            if Amax > Bmax:
                A.pop(AmaxIdx)
            else:
                B.pop(BmaxIdx)
            return F(A, B, lst)

    dap = F(A, B, [])
    print(len(dap))
    if dap:
        print(*dap)


if __name__ == '__main__':
    main()