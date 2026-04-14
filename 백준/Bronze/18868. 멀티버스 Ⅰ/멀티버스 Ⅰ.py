import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    M, N = map(int, input().split())
    lst = []
    for _ in range(M):
        lst.append(list(map(int, input().split())))
    dap = 0
    for i in range(M):
        for j in range(i+1, M):
            flag = True
            for k in range(N):
                for l in range(k+1, N):
                    if lst[i][k] < lst[i][l] and lst[j][k] >= lst[j][l]:
                        flag = False
                        break
                    elif lst[i][k] == lst[i][l] and lst[j][k] != lst[j][l]:
                        flag = False
                        break
                    elif lst[i][k] > lst[i][l] and lst[j][k] <= lst[j][l]:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                dap += 1
    print(dap)


if __name__ == '__main__':
    main()