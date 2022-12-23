# 행 N, 열 M 받기
N, M = map(int, input().split())
# 정사각형의 최대 크기 설정(행과 열 중 최소값)
maxSize = min(N,M)
# 직사각형 칸마다의 수 입력받음
lst = [list(map(int, list(input()))) for _ in range(N)]
# 답 초기화
dap = 1
# 행 순회
for n in range(N):
    # 열 순회
    for m in range(M):
        # 0부터 최대 크기까지 순회(정사각형 변 길이)
        for i in range(maxSize):
            # 직사각형 범위 안에 있고 네 꼭지점의 수가 모두 같다면
            if n+i<N and m+i<M and lst[n][m] == lst[n][m+i] == lst[n+i][m] == lst[n+i][m+i]:
                # 답과 정사각형 넓이 중 최대값을 답에 배정
                dap = max(dap, (i+1)**2)
# 답 출력
print(dap)