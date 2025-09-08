import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    if S[0] == '"' and S[-1] == '"':
        if S != '""' and S != '"':
            print(S[1:-1])
            return
    print('CE')


if __name__ == '__main__':
    main()