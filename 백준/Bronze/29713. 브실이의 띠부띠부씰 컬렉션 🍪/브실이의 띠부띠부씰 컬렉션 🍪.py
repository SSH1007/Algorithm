import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    D = input()
    lst = [0]*26
    for d in D:
        lst[ord(d)-65] += 1
    dap = 0
    while 1:
        flag = True
        for b in 'BRONZESILVER':
            lst[ord(b)-65] -= 1
            if lst[ord(b)-65] < 0:
                flag = False
                break
        if flag:
            dap += 1
        else:
            break
    print(dap)


if __name__ == '__main__':
    main()