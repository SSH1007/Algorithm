import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    T = input()

    def AB(st):
        if len(st) == len(S):
            if st == S:
                print(1)
                exit(0)
            return
        if st[-1] == 'A':
            AB(st[:-1])
        if st[0] == 'B':
            AB(st[::-1][:-1])
    AB(T)
    print(0)


if __name__ == '__main__':
    main()