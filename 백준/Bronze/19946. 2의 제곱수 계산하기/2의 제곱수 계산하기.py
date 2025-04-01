import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    cnt, flag = 1, False
    while N > 2:
        if N%2:
            N+=1
            flag = True
            cnt = 1
        N //= 2
        if flag:
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    main()