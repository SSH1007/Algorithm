import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t, p = map(int, input().split())
    if p > 20:
        x = t/(100-p)
        print((p-20)*x+20*x*2)
    else:
        x = t/((20-p)*2+80)
        print(p*x*2)


if __name__ == '__main__':
    main()