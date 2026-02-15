import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        _ = input()
        _, _ = map(int, input().split())
        Ns = list(map(int, input().split()))
        Ms = list(map(int, input().split()))
        strongest = max(max(Ns), max(Ms))
        n = Ns.count(strongest)
        m = Ms.count(strongest)
        print('S' if n >= m else 'B')


if __name__ == '__main__':
    main()