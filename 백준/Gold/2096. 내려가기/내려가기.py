import sys
input = sys.stdin.readline
from collections import deque


def main():
    N = int(input().rstrip())
    graph = list(map(int, input().rstrip().split()))
    dp1 = deque([[0]*3])
    dp2 = deque([[0]*3])
    dp1[0][0], dp1[0][1], dp1[0][2] = graph[0], graph[1], graph[2]
    dp2[0][0], dp2[0][1], dp2[0][2] = graph[0], graph[1], graph[2]
    for i in range(1, N):
        graph2 = list(map(int, input().rstrip().split()))
        tmp1, tmp2 = [], []
        for j in range(3):
            if j == 0:
                vMax = max(graph2[j] + dp1[0][j], graph2[j] + dp1[0][j+1])
                vMin = min(graph2[j] + dp2[0][j], graph2[j] + dp2[0][j+1])
                tmp1.append(vMax)
                tmp2.append(vMin)
            elif j == 1:
                vMax = max(graph2[j] + dp1[0][j-1], graph2[j] + dp1[0][j], graph2[j] + dp1[0][j+1])
                vMin = min(graph2[j] + dp2[0][j-1], graph2[j] + dp2[0][j], graph2[j] + dp2[0][j+1])
                tmp1.append(vMax)
                tmp2.append(vMin)
            elif j == 2:
                vMax = max(graph2[j] + dp1[0][j], graph2[j] + dp1[0][j-1])
                vMin = min(graph2[j] + dp2[0][j], graph2[j] + dp2[0][j-1])
                tmp1.append(vMax)
                tmp2.append(vMin)
        dp1.append(tmp1)
        dp1.popleft()
        dp2.append(tmp2)
        dp2.popleft()
    print(max(dp1[0]), min(dp2[0]))


if __name__ == '__main__':
    main()