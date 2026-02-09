import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    I = input()
    r = 0
    m = 0, 0
    for i in range(13):
        if I[i] == '*':
            m = 3 if i%2 else 1
            continue
        if i%2:
            r += int(I[i])*3
        else:
            r += int(I[i])
    for i in range(10):
        if (i*m+r)%10 == 0:
            print(i)
            return


if __name__ == '__main__':
    main()