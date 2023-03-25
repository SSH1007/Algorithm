N = int(input())
for _ in range(N):
    S = input()
    half = len(S)//2
    if S[half-1]==S[half]:
        print('Do-it')
    else:
        print('Do-it-Not')