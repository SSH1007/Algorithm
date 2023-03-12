# 2167번 : 2차원 배열의 합
# 구현 풀이 (PyPy3으로 해야 시간초과 안 됨)
'''
# 배열의 크기 N, M 입력
N, M = map(int, input().split())
# N*M 배열 입력
matrix = [list(map(int, input().split())) for _ in range(N)]
# 합을 구할 부분의 개수 K 입력
K = int(input())
# K만큼 반복
for _ in range(K):
    # 답 초기화
    dap = 0
    # (i,j)는 i행 j열을 의미. (x,y)는 x행 y열을 의미
    i, j, x, y = map(int, input().split())
    # 행 영역을 순회하면서
    for n in range(i-1, x):
        # 열 영역의 합을 답에 추가
        dap+=sum(matrix[n][j-1:y])
    print(dap)
'''

# 누적합 풀이
# 배열의 크기 N, M 입력
N, M = map(int, input().split())
# 메모이제이션용 리스트 초기화
memo = [[0 for _ in range(M+1)] for _ in range(N+1)]
# N*M 배열 입력
matrix = [list(map(int, input().split())) for _ in range(N)]

# 배열에 들어간 수들의 누적합을 각각 memo에 입력
for i in range(1, N+1):
    for j in range(1, M+1):
        memo[i][j] = memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1] + matrix[i-1][j-1]

# 합을 구할 부분의 개수 K 입력
K = int(input())
# i,j 위치부터 x,y위치까지에 저장되어 있는 수들의 합을 구하자
# 배열 (i,j) 위치 i행 j열을 나타낸다.
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(memo[x][y]-memo[i-1][y]-memo[x][j-1]+memo[i-1][j-1])