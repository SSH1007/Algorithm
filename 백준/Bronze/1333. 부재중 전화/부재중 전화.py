# 노래 수 N, 각 노래 길이 L, 전화벨은 D초당 1번씩 울림
N, L, D = map(int, input().split())
# 노래 총 시간 : L*1 + (L+5)*(N-1)
tmLine = [0]*(L+(L+5)*(N-1))

# 노래 N곡 순회
for n in range(N):
    # 노래 스타트 지점은 n*(L+5). 
    # n*를 해야 첫 시작은 5초의 빈 구간을 적용 안 할 수 있음
    start = n*(L+5)
    # 노래 시작부터 노래 끝날 때까지 tmLine의 구간을 체크
    for s in range(start, start+L):
        tmLine[s] = 1

# tmLine을 D초를 기준으로 순회 
for d in range(0, len(tmLine), D):
    # if tmLine[d]가 0이다(소리가 비어있다)
    if tmLine[d] == 0:
        # 그 시간을 출력하고 브레이크
        print(d)
        break
# 끝까지 돌렸는데 아귀가 안맞는다... 그러면
else:
    # tmLine 내에서 최종 도달한 시간에 D를 더해줘 출력
    print(d+D)