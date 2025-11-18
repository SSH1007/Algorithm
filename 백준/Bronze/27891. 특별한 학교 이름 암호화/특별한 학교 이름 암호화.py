import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    a = 'northlondo'
    b = 'branksomeh'
    c = 'koreainter'
    d = 'stjohnsbur'
    dap = ''
    for i in range(26):
        tmp = ''
        for n in N:
            tmp += chr(97+(ord(n)-97+i)%26)
        if tmp in [a, b, c, d]:
            dap = tmp
            break
    print(['NLCS', 'BHA', 'KIS', 'SJA'][[a, b, c, d].index(dap)])


if __name__ == '__main__':
    main()
