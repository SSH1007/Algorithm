T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    candies = list(map(int, input().split()))
    dap = [x//K for x in candies]
    print(sum(dap))