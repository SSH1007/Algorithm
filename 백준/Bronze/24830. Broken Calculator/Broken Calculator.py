import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    res = 1
    for _ in range(n):
        x, p, y = input().split()
        x, y = int(x), int(y)
        if p == '+':
            res = x+y-res
        elif p == '-':
            res = (x-y)*res
        elif p == '*':
            res = (x*y)**2
        else:
            if x%2 == 0:
                res = x//2
            else:
                res = (x+1)//2
        print(res)


if __name__ == '__main__':
    main()
