N, K = map(int,input().split())
arr = []
for i in range(1,N+1):
    if N%i==0:
        arr.append(i)
print(0 if len(arr)<K else arr[K-1])