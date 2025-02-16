import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        alpha = [0]*26
        S = input()
        for i in range(len(S)):
            if S[i] != ' ':
                alpha[ord(S[i])-97] += 1
        cnt, maxN, dap = 0, 0, 0
        for i in range(26):
            if alpha[i] > maxN:
                maxN = alpha[i]
                dap = i
        for i in range(26):
            if maxN == alpha[i]:
                cnt += 1
        if cnt > 1:
            print('?')
        else:
            print(chr(dap+97))


if __name__ == '__main__':
    main()