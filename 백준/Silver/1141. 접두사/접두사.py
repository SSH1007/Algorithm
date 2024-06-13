N = int(input())
S = set()
for _ in range(N):
    S.add(input())
S = sorted(list(S))
idx, dap = 0, 0
while idx < len(S)-1:
    if S[idx] == S[idx+1][:len(S[idx])]:
        idx += 1
    else:
        dap += 1
        idx += 1
print(dap+1)