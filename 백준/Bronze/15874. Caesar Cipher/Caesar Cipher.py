import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    k, s = map(int, input().split())
    S = input()
    dap = ''
    for i in range(s):
        if S[i].isalpha():
            if S[i].isupper():
                dap += chr((ord(S[i])-65+k)%26+65)
            else:
                dap += chr((ord(S[i])-97+k)%26+97)
        else:
            dap += S[i]
    print(dap)


if __name__ == '__main__':
    main()