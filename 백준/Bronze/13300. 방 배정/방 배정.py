import math

dic = dict()
N, K = map(int, input().split())     # N : 학생수, K: 한 방 당 수용 인원
for _ in range(N):
    S, Y = map(int, input().split()) # S : 성별, Y : 학년
    if (S, Y) not in dic.keys():
        dic[(S, Y)] = 1
    else:
        dic[(S, Y)] += 1

dap = 0
for v in dic.values():
    dap += math.ceil(v/K)

print(dap)