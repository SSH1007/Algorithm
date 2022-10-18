import sys
input = sys.stdin.readline

N = input().strip().split('-')
arr = []
for n in N:
    lst = list(map(int, n.split('+')))
    arr.append(sum(lst))
dap = arr[0]
for a in range(1,len(arr)):
    dap-=arr[a]
print(dap)