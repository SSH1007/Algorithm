N = int(input())
K = 1
while 1:
    if N == 1+K+K**2:
        break
    K+=1
print(K)