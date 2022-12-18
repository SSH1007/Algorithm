import sys
input = sys.stdin.readline
# 한변의 길이 N 입력
N = int(input())
# 하얀 색종이와 파란 색종이 개수 초기화
white, blue = 0, 0 

# 분할정복 함수 정의
def z(n,r,c):
    # 전역 변수로 각 색종이들의 개수를 받음
    global white, blue
    # (r,c) 위치의 색종이 색깔 'color'를 받는다
    color = graph[r][c]
    # 범위 내의 색종이 색깔들을 하나씩 검사해보다가
    for row in range(r,r+n):
        for col in range(c,c+n):
            # 'color'와 다른 색이 나오면
            if graph[row][col] != color:
                # 1사분면
                z(n//2,r,c)
                # 2사분면
                z(n//2,r,c+n//2)
                # 3사분면
                z(n//2,r+n//2,c)
                # 4사분면
                z(n//2,r+n//2,c+n//2)
                # 으로 동일 작업을 반복한 뒤 반환
                return
    # 'color'가 1이면 파란색 개수 +=1
    if color == 1:
        blue+=1
    # 아니면 하얀색 개수 += 1
    elif color == 0:
        white+=1

# 색종이들의 색을 의미하는 행렬 입력 받음
graph = [list(map(int,input().split())) for _ in range(N)]
# 함수 실행
z(N,0,0)
print(white)
print(blue)