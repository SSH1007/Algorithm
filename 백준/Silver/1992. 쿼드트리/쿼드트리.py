# 분할 정복 - 재귀 : 2630. 색종이 만들기와 유사
import sys
input = sys.stdin.readline
N = int(input().rstrip())
graph = [list(map(int, list(input().rstrip()))) for _ in range(N)]

lst = []
def QuadTree(n, r, c):
    number = graph[r][c]
    for row in range(r, r+n):
        for col in range(c, c+n):
            if graph[row][col] != number:
                print('(', end='')
                QuadTree(n//2, r, c)
                QuadTree(n//2, r, c+n//2)
                QuadTree(n//2, r+n//2, c)
                QuadTree(n//2, r+n//2, c+n//2)
                print(')', end='')
                return
    print(number, end='')
    lst.append(number)
QuadTree(N, 0, 0)