# N명의 친구들
# 한 사람이 공을 M번 받으면 게임은 끝
# 자기 위치로부터 L만큼 떨어져 있는 사람에게 던진다
N, M, L = map(int, input().split())
# N명의 친구들이 공을 받은 횟수를 저장하는 리스트 생성
friend = [0 for _ in range(N+1)]
# 첫번째 친구는 이미 한번 받은 걸로 시작
start = 1
friend[start] = 1
while 1:
    # 받은 횟수가 M이 되면 브레이크
    if friend[start] == M:
        break
    # 받은 횟수가 홀수면
    if friend[start]%2:
        # 시계방향으로 L만큼 떨어진 친구에게 던짐
        start+=L
        start%=N
        friend[start] += 1
    # 받은 횟수가 짝수면
    else:
        # 반시계방향으로 L만큼 떨어진 친구에게 던짐
        start-=L
        start%=N
        friend[start] += 1
# 총 던진 횟수 출력
print(sum(friend)-1)
