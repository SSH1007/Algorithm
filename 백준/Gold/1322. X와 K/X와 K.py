import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    N_bin = list(bin(N)[2:])
    K_bin = list(bin(K)[2:])
    dap = ''
    #   101
    #    1
    #  1 0
    #  1 1
    # 10 0
    # 10 1
    # print(int('10010',2))  # 5+18 == 5|18
    while N_bin:
        back = N_bin.pop()
        if back == '0':
            if K_bin:
                dap = K_bin.pop() + dap
        else:
            dap = '0' + dap
    print(int(''.join(K_bin) + dap, 2))


if __name__ == '__main__':
    main()