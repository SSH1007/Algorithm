import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {1:1, 2:2}

    def fibo(n):
        if n in dic:
            return dic[n]
        dic[n] = fibo(n-1)+fibo(n-2)
        return dic[n]

    fibo(486)
    while 1:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        dap = 0
        for i in range(1, 486):
            if a <= dic[i] <= b:
                dap += 1
            if dic[i]>b:
                break
        print(dap)


if __name__ == '__main__':
    main()