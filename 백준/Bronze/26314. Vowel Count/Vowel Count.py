import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        nm = input()
        c = 0
        for m in nm:
            if m in 'aeiou':
                c += 1
        print(nm)
        print(1 if c > len(nm)-c else 0)


if __name__ == '__main__':
    main()