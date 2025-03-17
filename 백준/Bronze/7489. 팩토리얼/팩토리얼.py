import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        a = 1
        for n in range(1, N+1):
            a *= n
            while a%10==0:
                a//=10
            a%=10000
        print(str(a)[-1])


if __name__ == '__main__':
    main()