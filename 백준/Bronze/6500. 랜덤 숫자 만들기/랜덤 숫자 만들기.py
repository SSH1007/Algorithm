import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        n = int(input())
        s = set()
        if n == 0:
            break
        s.add(n)
        while 1:
            tmp = (n*n//100)%10000
            if tmp in s:
                break
            s.add(tmp)
            n = tmp
        print(len(s))


if __name__ == '__main__':
    main()