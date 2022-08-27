yc = int(input())
ys = list(map(int, input().split()))
ys.sort()
print(ys[0]*ys[-1])