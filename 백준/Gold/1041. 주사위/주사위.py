import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    a, b, c, d, e, f = map(int, input().split())
    dice = sorted([a, b, c, d, e, f])
    three = [a+b+c, a+b+d, a+e+d, a+e+c,
            c+e+f, c+b+f, f+b+d, e+f+d]
    two = [a+c, a+b, a+d, a+e,
           c+b, b+d, d+e, e+c,
           c+f, b+f, d+f, e+f]
    one = [a+b+c+d+e, a+b+c+d+f, a+b+c+e+f, a+b+d+e+f, a+c+d+e+f, b+c+d+e+f]
    if N == 1:
        print(min(one))
    else:
        # 맨 위 층
        top = 0
        # 3*4
        top += min(three)*4
        # 2*(N-2)
        top += min(two)*(N-2)*4
        # 1*(N-2)**2
        top += dice[0]*((N-2)**2)
        # 나머지 층 * (N-1)
        other = 0
        # 2*4
        other += min(two)*4
        # 1*(N-2)*4
        other += dice[0]*(N-2)*4
        print(top + other*(N-1))


if __name__ == '__main__':
    main()