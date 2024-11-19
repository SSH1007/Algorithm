import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N, M = input().split()
        o, z = 0, 0
        for i in range(len(N)):
            if N[i] != M[i]:
                if N[i] == '0':
                    z += 1
                else:
                    o += 1
        print(max(o, z))


if __name__ == '__main__':
    main()