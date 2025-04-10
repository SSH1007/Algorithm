import sys
input = lambda: sys.stdin.readline().rstrip()


def F(S):
    if len(S) != 7:
        return False
    if S[0]==S[1]==S[4] and S[2]==S[3]==S[5]==S[6] and S[0] != S[2]:
        return True
    return False


def main():
    T = int(input())
    for _ in range(T):
        S = input()
        print(1 if F(S) else 0)


if __name__ == '__main__':
    main()