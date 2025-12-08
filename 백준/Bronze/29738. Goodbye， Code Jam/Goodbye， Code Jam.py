import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    r, y = ['Round 1', 'Round 2', 'Round 3', 'World Finals'], 0
    for t in range(1, T+1):
        N = int(input())
        if N > 4500:
            y = 0
        elif N > 1000:
            y = 1
        elif N > 25:
            y = 2
        else:
            y = 3
        print(f'Case #{t}: {r[y]}')


if __name__ == '__main__':
    main()