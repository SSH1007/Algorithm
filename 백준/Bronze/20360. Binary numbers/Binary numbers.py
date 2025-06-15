import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    B = bin(n)
    L = len(B)
    for i in range(L-1, -1, -1):
        if B[i] == '1':
            print(L-i-1, end=' ')


if __name__ == '__main__':
    main()