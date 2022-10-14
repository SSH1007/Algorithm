# DFS 문제(재귀) - 백트래킹
N = int(input())
As = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
min_ = int(1e9)
max_ = -int(1e9)

def dfs(order, hap, add, sub, mul, div):
    global min_, max_
    if order == N:
        min_ = min(hap, min_)
        max_ = max(hap, max_)
        return
    
    if add:
        dfs(order+1, hap+As[order], add-1, sub, mul, div)
    if sub:
        dfs(order+1, hap-As[order], add, sub-1, mul, div)
    if mul:
        dfs(order+1, hap*As[order], add, sub, mul-1, div)
    if div:
        dfs(order+1, int(hap/As[order]), add, sub, mul, div-1)

dfs(1, As[0], add, sub, mul, div)
print(max_, min_, sep='\n')