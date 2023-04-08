# N : 바구니 수, M : 회전 횟수
N, M = map(int, input().split())
baskets = [i for i in range(0,N+1)]
for _ in range(M):
    begin, end, mid = map(int, input().split())
    baskets = baskets[:begin]+baskets[mid:end+1]+baskets[begin:mid]+baskets[end+1:]
print(*baskets[1:])