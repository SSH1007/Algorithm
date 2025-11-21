import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    s = set()
    for n in range(N):
        tmp = ord(S[n])-65
        if tmp not in s:
            s.add(tmp)
    print('Yes' if len(s) > 2 else 'No')


if __name__ == '__main__':
    main()