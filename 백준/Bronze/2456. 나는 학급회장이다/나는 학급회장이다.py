N = int(input())
candidate = [[i+1, 0,0,0,0] for i in range(3)]
for _ in range(N):
    a, b, c = map(int, input().split())
    candidate[0][a] += 1
    candidate[1][b] += 1
    candidate[2][c] += 1


for cand in candidate:
    for i in range(1,4):
        cand[4] += cand[i]*(i)

candidate.sort(key=lambda x : (-x[4], -x[3], -x[2], -x[1]))

if candidate[0][2:] == candidate[1][2:]:
    print(0, candidate[0][4])
else:
    print(candidate[0][0], candidate[0][4])