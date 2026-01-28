import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        S = input()
        lst = [0]*5
        if N >= 12:
            lst[4] = 1
        for n in range(N):
            if S[n].islower():
                lst[0] = 1
            elif S[n].isupper():
                lst[1] = 1
            elif S[n].isdecimal():
                lst[2] = 1
            elif S[n] in '+_)(*&^%$#@!./,;{}':
                lst[3] = 1
        print('valid' if sum(lst) == 5 else 'invalid')


if __name__ == '__main__':
    main()