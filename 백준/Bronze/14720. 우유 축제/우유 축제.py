# 우유 가게의 수 N 입력
N = int(input())
# 우유 마신 개수 초기화
drunk = 0
# 0:딸기우유, 1:초코우유, 2:바나나우유
milkStoreInfo = list(map(int, input().split()))
# 우유가게 순회하면서 
for i in range(N):
    # 0,1,2이 반복된다. 
    # = 현재까지 마신 우유 수를 3으로 나눈 나머지 값이 다음에 마실 우유의 종류를 의미
    if milkStoreInfo[i] == drunk%3:
        drunk+=1
print(drunk)