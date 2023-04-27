def fun():
    import sys
    input = sys.stdin.readline
    N = int(input().rstrip())
    dic = dict()
    for _ in range(N):
        a, b = input().rstrip().split()
        if b == 'enter':
            dic[a] = 1
        else:
            dic[a] = 0
    dap = [x for x in list(dic.items()) if x[1] == 1]
    dap2 = sorted(dap, reverse = True)
    for d in dap2:
        print(d[0])

if __name__ == '__main__':
    fun()