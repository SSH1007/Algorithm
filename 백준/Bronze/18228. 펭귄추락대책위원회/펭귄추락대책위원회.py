import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    penguin = 0
    for i in range(N):
        if As[i] == -1:
            penguin = i
    print(min(As[:penguin])+min(As[penguin+1:]))


if __name__ == '__main__':
    main()