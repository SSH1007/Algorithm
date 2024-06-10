from collections import defaultdict

def f(n, prime):
    idx = 0
    mom = list(prime.keys())[:65]
    cnt = 0
    while n != 1:
        if idx >= 65:
            return cnt+1
        if n%mom[idx] == 0:
            n//=mom[idx]
            cnt += 1
        else:
            idx += 1
    return cnt


def main():
    Max = int(100000**0.5)
    lst = [1]*Max
    for i in range(2, Max):
        if lst[i]:
           for j in range(i*2, Max, i):
               lst[j] = 0
    prime = defaultdict(int)
    for i in range(2, Max):
        if lst[i]:
            prime[i] = 1
    dap = 0
    A, B = map(int, input().split())
    for C in range(A, B+1):
        if prime[f(C, prime)]:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()