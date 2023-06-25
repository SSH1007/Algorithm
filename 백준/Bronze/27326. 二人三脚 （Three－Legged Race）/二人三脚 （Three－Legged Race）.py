import sys
input = sys.stdin.readline
N = int(input().rstrip())
jo = [0]*N
lst = list(map(int, input().rstrip().split()))
for l in lst:
    jo[l-1]+=1
print(jo.index(1)+1)