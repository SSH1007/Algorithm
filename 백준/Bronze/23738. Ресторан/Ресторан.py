import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {'B':'v', 'E':'ye', 'H':'n', 'P':'r', 'C':'s', 'Y':'u', 'X':'h'}
    S = input()
    dap = ''
    for s in S:
        if s in dic:
            dap += dic[s]
        else:
            dap += s.lower()
    print(dap)


if __name__ == '__main__':
    main()