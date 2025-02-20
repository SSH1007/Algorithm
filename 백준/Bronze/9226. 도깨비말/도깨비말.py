import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    mo = ['a', 'e', 'i', 'o', 'u']
    while 1:
        S = input()
        if S == '#':
            break
        idx = 0
        for i in range(len(S)):
            if S[i] in mo:
                idx = i
                break
        print(S[idx:]+S[:idx]+'ay')


if __name__ == '__main__':
    main()