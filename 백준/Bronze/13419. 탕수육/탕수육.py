T = int(input())
for _ in range(T):
    S = input()
    if len(S)%2 == 0:
        print(S[::2])
        print(S[1::2])
    else:
        print(S[::2]+S[1::2])
        print(S[1::2]+S[::2])