import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    if M < 27:
        d = chr(M+64)
    else:
        t = M-26
        d = chr((t-1)//26+97)+chr((t-1)%26+97)
    print(f'SN {N}{d}')


if __name__ == '__main__':
    main()