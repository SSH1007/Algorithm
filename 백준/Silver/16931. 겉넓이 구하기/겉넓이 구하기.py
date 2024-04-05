import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
paper = [list(map(int, input().rstrip().split())) for _ in range(N)]
dap = 0


def F(lst):
    dap = 0
    for n in range(len(lst)):
        tmp = lst[n][0]
        for m in range(1, len(lst[0])):
            if lst[n][m] > lst[n][m-1]:
                tmp += (lst[n][m] - lst[n][m-1])
        dap += tmp
    return dap


dap += F(paper)
paper2 = list(map(list, zip(*paper[::-1])))
dap += F(paper2)
paper3 = list(map(list, zip(*paper2[::-1])))
dap += F(paper3)
paper4 = list(map(list, zip(*paper3[::-1])))
dap += F(paper4)
dap += (N*M*2)
print(dap)