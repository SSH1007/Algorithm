import sys
sys.setrecursionlimit(1000)
input = sys.stdin.readline
N, S = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
nums = []
cnt = 0

def DFS(lst, nums, start):
    global cnt
    if nums and sum(nums) == S:
        cnt += 1
    for i in range(start, len(lst)):
        nums.append(lst[i])
        DFS(lst, nums, i+1)
        nums.pop()


DFS(lst, nums, 0)
print(cnt)