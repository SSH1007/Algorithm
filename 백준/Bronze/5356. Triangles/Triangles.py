import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for n in range(N):
        if n != 0:
            print()
        x, y = input().split()
        for i in range(1, int(x)+1):
            print(y*i)
            y = chr((ord(y)-65+1)%26+65)


if __name__ == '__main__':
    main()