import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    N = int(input())
    lst = []
    for _ in range(N):
        x, y = map(int, input().split())
        lst.append((x, y))
    lst.sort()
    s, e = lst[0][0], lst[0][1]
    dap = e-s
    for i in range(1, N):
        x, y = lst[i][0], lst[i][1]
        # 1. s~e 안에 x~y가 포함될 때
        if s <= x and y <= e:
            continue
        # 2. s~e와 x~y가 겹칠 때
        elif e >= x:
            dap += (y-e)
            e = y
        # 3. s~e의 범위를 x~y가 벗어날 때
        elif e < x:
            s, e = x, y
            dap += (e-s)
    print(dap)


if __name__ == '__main__':
    main()