import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(1, N+1):
        C = int(input())
        cnt = 0
        lst = list(input().split())
        for c in range(C):
            if lst[c] == 'sheep':
                cnt += 1
        print(f'Case {n}: This list contains {cnt} sheep.')
        print()


if __name__ == '__main__':
    main()