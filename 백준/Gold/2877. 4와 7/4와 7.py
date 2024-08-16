import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    K = int(input())
    cnt = 1
    tmp = 0
    while 1:
        tmp += 2**cnt
        if K <= tmp:
            break
        cnt += 1
    tmp -= 2**cnt
    result = bin(K-tmp-1)[2:].zfill(cnt)
    dap = ''
    for r in result:
        if r == '0':
            dap += '4'
        else:
            dap += '7'
    print(dap)


if __name__ == '__main__':
    main()