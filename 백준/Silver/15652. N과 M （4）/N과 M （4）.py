N, M = map(int, input().split())
# 수열을 표시할 빈 리스트 정의
sy = []
# dfs 함수 정의
def dfs(start):
    # 백트래킹 설정(수열의 길이가 M일 경우 = 자연수 중 M개를 골랐을 때)
    if len(sy) == M:
        # 수열을 출력하고 반환
        print(*sy)
        return
    # 중복되는 수열을 출력하지 않기 위해 start의 값을 계속 증가시키면서(체크 범위 줄이기) dfs 실행
    for n in range(start,N+1):
        # 수열에 비내림차순으로 숫자를 골라 추가
        sy.append(n)
        dfs(n)
        # M개 골라서 수열 출력한 이후에는 숫자를 다시 빼준다(무한재귀 방지 용도).
        sy.pop()
# dfs 함수 실행
dfs(1)