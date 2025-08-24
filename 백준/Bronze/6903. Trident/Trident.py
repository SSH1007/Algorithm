import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = int(input())
    s = int(input())
    h = int(input())
    for _ in range(t):
        print('*'+' '*s+'*'+' '*s+'*')
    print('*'*(3+2*s))
    for _ in range(h):
        print(' '*(1+s)+'*')


if __name__ == '__main__':
    main()