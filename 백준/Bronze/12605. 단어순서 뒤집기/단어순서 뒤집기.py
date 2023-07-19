N = int(input())
for n in range(1, N+1):
    S = list(input().split())
    nS = S[::-1]
    print('Case #', n, ': ', ' '.join(nS), sep='')