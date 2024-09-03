import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    money = int(input())
    J, S = money, money
    J_s, S_s = 0, 0
    stock = list(map(int, input().split()))

    for i in range(13):
        if stock[i] <= J:
            J, J_s = J%stock[i], J_s+J//stock[i]

    for i in range(3, 13):
        if stock[i-1] > stock[i-2] > stock[i-3]:
            # 매도
            S, S_s = S+S_s*stock[i], 0
        elif stock[i-1] < stock[i-2] < stock[i-3]:
            if stock[i] <= S:
                # 매수
                S, S_s = S%stock[i], S_s+S//stock[i]
    J_m = J+J_s*stock[13]
    S_m = S+S_s*stock[13]
    if J_m > S_m:
        print("BNP")
    elif J_m < S_m:
        print("TIMING")
    else:
        print("SAMESAME")


if __name__ == '__main__':
    main()