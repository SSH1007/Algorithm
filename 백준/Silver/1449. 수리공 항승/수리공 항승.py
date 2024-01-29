N, L = map(int, input().split())
pipe = [0]*(2001)
tape = sorted(list(map(int, input().split())))
cnt = 0
for t in tape:
    if not pipe[t]:
        for i in range(t, t+L):
            pipe[i] = 1
        cnt += 1
print(cnt)