import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        lst = [input() for _ in range(N)]
        lst.sort()
        for n in range(N-1):
            if lst[n][:len(lst[n])] == lst[n+1][:len(lst[n])]:
                print('NO')
                break
        else:
            print('YES')


if __name__ == '__main__':
    main()