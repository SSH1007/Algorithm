# set, dictionary은 해시로 찾기 때문에 list보다 찾는 속도가 빠르다
N = int(input())
nset = set(map(int,input().split()))
M = int(input())
mlst = list(map(int, input().split()))
for m in mlst:
    print(1 if m in nset else 0, end=' ')