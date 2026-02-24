import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        N = int(input())
        if N == 0:
            break
        idx = 0
        for _ in range(N):
            S = input()+' '
            for i in range(idx, len(S)):
                if S[i] == ' ':
                    idx = i
                    break
        print(idx+1)


if __name__ == '__main__':
    main()