import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A, B, C, D = map(int, input().split())
    S = input()
    if S[0] != 'a' or S[-1] != 'a':
        print('No')
        return
    for n in range(N-1):
        if S[n] == S[n+1]:
            print('No')
            return
        else:
            if S[n] == 'a':
                A -= 1
            elif S[n] == 'b':
                B -= 1
            elif S[n] == 'c':
                C -= 1
            else:
                D -= 1
    if A < 0 or B < 0 or C < 0 or D <0:
        print('No')
        return
    print('Yes')


if __name__ == '__main__':
    main()