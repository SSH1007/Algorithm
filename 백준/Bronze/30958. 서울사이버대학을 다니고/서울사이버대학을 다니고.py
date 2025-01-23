import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    alp = [0]*26
    for n in range(N):
        if S[n].isalpha():
            alp[ord(S[n])-96] += 1
    print(alp[alp.index(max(alp))])


if __name__ == '__main__':
    main()