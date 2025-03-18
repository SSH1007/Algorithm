import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    odd, even = [], []
    for n in range(N):
        if As[n] % 2:
            odd.append(As[n])
        else:
            even.append(As[n])
    dap = sum(even)
    odd.sort()
    while len(odd)>1:
        a = odd.pop()
        b = odd.pop()
        dap += (a+b)
    print(dap)


if __name__ == '__main__':
    main()