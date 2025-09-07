import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    H = int(input())*100
    W = int(input())*100
    print(min(H, W)//2)


if __name__ == '__main__':
    main()