import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        lst = [0 for _ in range(10)]
        try:
            N = int(input())
            k = 1
            while 1:
                n = N*k
                while n > 0:
                    tmp = n % 10
                    lst[tmp] = 1
                    n //= 10
                if sum(lst) == 10:
                    print(k)
                    break
                k += 1
        except:
            break


if __name__ == '__main__':
    main()