def QueenCan(x):
    for i in range(x):
        # row[x]과 row[i]가 같다 = 같은 열에 두 개 이상의 퀸이 존재한다.
        # abs(row[x]-row[i])==x-i는 A(x,row[x])와 B(i,row[i])가 같은 대각선 상에 존재한다는 뜻
        if row[x] == row[i] or abs(row[x]-row[i])==x-i:
            return False
    return True

# dfs 함수
def dfs(x):
    global dap
    # 만약 x가 N과 같다면(0부터 N번째 행까지 다 확인했다면)
    if x==N:
        dap+=1
        return
    else:
        # N번 순회
        for i in range(N):
            # x번째 행의 i번째 열에 퀸을 놓는다
            row[x] = i
            # 퀸들이 서로 공격할 수 없다면
            if QueenCan(x):
                # 다음 행으로 넘어가 dfs 함수 실행
                dfs(x+1)


# 체스판 크기, 퀸 개수를 결정하는 N 받기
N = int(input())
# row의 x번째 값이 y이다 = (x,y)에 퀸이 있다
# 파이썬에서 리스트는 0부터 시작하므로 순번을 맞추기 위해 N+1개의 [0] 생성
row = [0]*(N+1)
# dap(경우의 수) 초기화
dap = 0
# dfs 함수 실행
dfs(0)
# nQueen 경우의 수 출력
print(dap)