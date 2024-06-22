import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())

    def isPrime(n):
        if n == 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def DFS(s, idx):
        if s != '' and not isPrime(int(s)):
            return
        if idx == N:
            print(s)
            return
        for i in range(1, 10):
            DFS(s+str(i), idx+1)

    DFS('', 0)


if __name__ == '__main__':
    main()