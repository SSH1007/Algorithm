R, B = map(int, input().split())
entire = R+B
L, W = 0, 0
for i in range(3, int(entire**0.5)+1):
    if entire % i == 0:
        W = i
        L = entire//i
        if (W-2)*(L-2) == B:
            break
print(L, W)