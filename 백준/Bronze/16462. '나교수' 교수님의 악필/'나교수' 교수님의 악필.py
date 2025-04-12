import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    x = 0
    for _ in range(N):
        Q = input()
        s = ''
        for q in Q:
            if q in ['0', '6', '9']:
                s += '9'
            else:
                s += q
        x += min(int(s), 100)
    x /= N
    print(int(x)+1 if x%1>=0.5 else int(x))


if __name__ == '__main__':
    main()