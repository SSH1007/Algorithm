import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    i = len(S)-1
    while 1:
        if set(S[:i]) == set(S[i:]):
            break
        i -= 1
    print(i)


if __name__ == '__main__':
    main()