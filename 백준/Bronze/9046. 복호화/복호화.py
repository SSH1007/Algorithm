import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        alpha = [0]*26
        S = input().replace(" ", "")
        for i in range(len(S)):
            alpha[ord(S[i])-97] += 1
        if alpha.count(max(alpha)) > 1:
            print("?")
        else:
            print(chr(alpha.index(max(alpha))+97))


if __name__ == '__main__':
    main()