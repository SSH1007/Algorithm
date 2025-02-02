import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    S = input()
    lst = [0]*26
    for i in range(len(S)):
        lst[ord(S[i])-97] += 1
    dap =1000
    for i in ['u','o','s','p','c']:
        tmp = lst[ord(i)-97]
        if dap > tmp:
            dap = tmp
    print(dap)


if __name__ == '__main__':
    main()