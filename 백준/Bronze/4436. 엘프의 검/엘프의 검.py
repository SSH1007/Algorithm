import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        try:
            N, k = int(input()), 1
            check = 0
            while 1:
                for n in str(N*k):
                    check |= (1 << int(n))
                if check == 1023:
                    print(k)
                    break
                k += 1
        except:
            exit(0)


if __name__ == '__main__':
    main()