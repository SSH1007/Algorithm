import sys
input = sys.stdin.readline


def main():
    N = int(input().rstrip())

    def isPrime(n):
        i = 2
        while i*i <= n:
            if n % i == 0:
                return False
            else:
                i += 1
        return True

    def DFS(s, idx):
        if s != '' and not isPrime(int(s)):
            return
        if idx == N:
            print(s)
            return
        for i in range(10):
            if idx < 1 and i <= 1:
                continue
            DFS(s+str(i), idx+1)

    DFS('', 0)


if __name__ == '__main__':
    main()