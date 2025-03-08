import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = 1
    while 1:
        S = input()
        if S == "Was it a cat I saw?":
            break
        for i in range(0, len(S), t+1):
            print(S[i], end='')
        print()
        t += 1


if __name__ == '__main__':
    main()