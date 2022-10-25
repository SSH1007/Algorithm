import sys
input = sys.stdin.readline
N = int(input())
white, blue = 0, 0 

def z(n,r,c):
    global white, blue
    color = graph[r][c]
    for row in range(r,r+n):
        for col in range(c,c+n):
            if graph[row][col] != color:
                z(n//2,r,c)
                z(n//2,r,c+n//2)
                z(n//2,r+n//2,c)
                z(n//2,r+n//2,c+n//2)
                return
    if color == 1:
        blue+=1
    elif color == 0:
        white+=1

graph = [list(map(int,input().split())) for _ in range(N)]
z(N,0,0)
print(white)
print(blue)