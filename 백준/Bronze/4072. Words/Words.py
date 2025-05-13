import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        I = input()
        if I == '#':
            break
        lst = I.split()
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        print(' '.join(lst))


if __name__ == '__main__':
    main()