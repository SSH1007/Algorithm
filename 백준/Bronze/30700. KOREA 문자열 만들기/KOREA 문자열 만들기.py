import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    K = ['K', 'O', 'R', 'E', 'A']
    j = 0
    tmp = ''
    for i in range(len(S)):
        if S[i] == K[j]:
            tmp += S[i]
            j = (j+1)%5
    print(len(tmp))


if __name__ == '__main__':
    main()