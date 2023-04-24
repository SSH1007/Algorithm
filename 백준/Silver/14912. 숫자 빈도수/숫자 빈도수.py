def dap():
    n, d = map(int, input().split())
    dap = 0
    for i in range(1, n+1):
        dap+=str(i).count(str(d))
    print(dap)

if __name__ == '__main__':
    dap()