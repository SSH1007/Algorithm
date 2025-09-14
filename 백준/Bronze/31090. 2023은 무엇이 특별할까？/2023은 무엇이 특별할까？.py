import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = input()
        n = int(N)
        if (n+1)%int(N[-2:]) == 0:
            print('Good')
        else:
            print('Bye')


if __name__ == '__main__':
    main()