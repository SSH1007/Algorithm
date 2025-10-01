import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    fib = [0]*491
    fib[1], fib[2] = 1, 1
    for i in range(3, 491):
        fib[i] = fib[i-1] + fib[i-2]
    while 1:
        N = int(input())
        if N == -1:
            break
        print(f'Hour {N}: {fib[N]} cow(s) affected')


if __name__ == '__main__':
    main()