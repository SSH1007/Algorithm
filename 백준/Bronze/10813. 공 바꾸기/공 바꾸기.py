# 10813번: 공 바꾸기
# 바구니의 개수 N, 공을 바꾸는 횟수 M 입력
N, M = map(int, input().split())
# 각각의 바구니에는 1번부터 N번까지 번호가 매겨져 있음(0~N까지의 N+1 크기의 리스트)
baskets = [n for n in range(N+1)]
# M번 동안 공을 바꿀 바구니 2개 입력
for _ in range(M):
    a,b = map(int, input().split())
    # swap 교환 
    baskets[a], baskets[b] = baskets[b], baskets[a]
# 1번 바구니부터 N번 바구니에 들어있는 공의 번호 출력
print(*baskets[1:])