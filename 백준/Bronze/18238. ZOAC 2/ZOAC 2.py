import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    start, acc = 0, 0
    for s in S:
        c = ord(s)-65
        m = (start-c)%26
        n = 26-m
        acc += m if m < n else n
        start = c
    print(acc)


if __name__ == '__main__':
    main()