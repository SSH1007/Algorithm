import sys
input = lambda: sys.stdin.readline().rstrip()


def F(S):
    if len(S) > 10:
        return 0
    if sum([s.isdecimal() for s in S]) == len(S):
        return 0
    if sum([s.isupper() for s in S]) > sum([s.islower() for s in S]):
        return 0
    return 1


def main():
    N = int(input())
    for _ in range(N):
        S = input()
        if F(S):
            print(S)


if __name__ == '__main__':
    main()