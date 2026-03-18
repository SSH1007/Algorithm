import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dic = dict()
    for _ in range(N):
        a, b = input().split()
        dic[b] = a
    T = input()
    d = ''
    for t in T:
        d += dic[t]
    S, E = map(int, input().split())
    print(d[S-1:E])


if __name__ == '__main__':
    main()