import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t = 1000
    maps = [[0]*2000 for _ in range(2000)]
    a,b,c,d = map(int, input().split())
    e,f,g,h = map(int, input().split())
    w,x,y,z = map(int, input().split())
    for i in range(t+a, t+c):
        for j in range(t+b, t+d):
            maps[i][j] = 1
    for i in range(t+e, t+g):
        for j in range(t+f, t+h):
            maps[i][j] = 1
    for i in range(t+w, t+y):
        for j in range(t+x, t+z):
            maps[i][j] = 0
    dap = 0
    for m in maps:
        dap += sum(m)
    print(dap)


if __name__ == '__main__':
    main()