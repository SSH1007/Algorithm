import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for t in range(1, T+1):
        H, M = map(int, input().split())
        print(f'Case #{t}: {H if M >= 45 else (H-1)%24} {(M-45)%60}')


if __name__ == '__main__':
    main()