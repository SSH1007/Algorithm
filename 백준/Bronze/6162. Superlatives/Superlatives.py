import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    K = int(input())
    for k in range(1, K+1):
        A, E = map(int, input().split())
        print(f'Data Set {k}:')
        c = 0
        tmp = A/E
        for i in range(8, 0, -1):
            if tmp > 5**i:
                c = i
                break
        print(('mega '*c if tmp > 1 else 'no ') + 'drought')
        print()


if __name__ == '__main__':
    main()