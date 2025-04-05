import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {"A": 4, "B": 3, "C": 2, "D": 1, "F": 0, "+":0.5}
    S = list(input())
    dap, cnt = 0, 0
    for i in range(len(S)):
        dap += dic[S[i]]
        if S[i] != "+":
            cnt += 1
    print(dap/cnt)


if __name__ == '__main__':
    main()