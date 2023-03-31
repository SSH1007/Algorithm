T = int(input())
cnt = 0
for _ in range(T):
    if cnt:
        print()
    cnt+=1
    N = int(input())
    for i in range(N):
        for j in range(N):
            if i == 0 or j == 0 or i==N-1 or j==N-1:
                print('#', end='')
            else:
                print('J', end='')
        print()