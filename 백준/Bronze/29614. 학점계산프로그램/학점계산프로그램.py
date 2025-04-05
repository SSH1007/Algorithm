import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {"A+": 4.5, "A": 4.0, "B+": 3.5, "B": 3.0, "C+": 2.5, "C": 2.0, "D+": 1.5, "D": 1.0, "F": 0.0}
    S = list(input())
    dap, cnt = 0, 0
    while S:
        if S[-1] == '+':
            a = S.pop()
            b = S.pop()
            tmp = b+a
        else:
            tmp = S.pop()
        dap += dic[tmp]
        cnt += 1
    print(dap/cnt)


if __name__ == '__main__':
    main()