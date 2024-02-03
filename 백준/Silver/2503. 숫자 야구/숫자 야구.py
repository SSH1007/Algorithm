# 1부터 9까지의 중복되지 않는 수열(순열)을 만든다
from itertools import permutations
AllNum = [''.join(i) for i in permutations(map(str, range(1, 10)), 3)]
N = int(input())
for _ in range(N):
    GuessNum, Strike, Ball = map(int, input().split())
    GuessNum = str(GuessNum)
    removeCnt = 0
    for i in range(len(AllNum)):
        s_cnt, b_cnt = 0, 0
        idx = i-removeCnt
        for j in range(3):
            # 스트라이크 판별
            if GuessNum[j] == AllNum[idx][j]:
                s_cnt += 1
            # 볼 판별
            elif GuessNum[j] in AllNum[idx]:
                b_cnt += 1
        # 스트라이크가 안 맞거나, 볼이 안 맞으면 다음 순회 때 볼 필요가 없으므로 remove로 제거
        if s_cnt != Strike or b_cnt != Ball:
            AllNum.remove(AllNum[idx])
            # removeCnt를 1 더해주는 걸로 짧아진 AllNum에 맞게 idx를 맞춘다.
            removeCnt += 1
print(len(AllNum))