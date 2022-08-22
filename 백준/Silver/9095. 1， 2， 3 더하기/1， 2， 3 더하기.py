T = int(input())
for _ in range(T):
    arr = [1,2,4]
    N = int(input())
    arr = arr+[0]*(N-3)
    for i in range(N):
        if i<3:
            pass
        else:
            arr[i] = arr[i-1]+arr[i-2]+arr[i-3]
    print(arr[N-1])