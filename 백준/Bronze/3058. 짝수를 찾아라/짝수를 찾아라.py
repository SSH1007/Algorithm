T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    lst = [i for i in lst if i%2==0]
    minN = min(lst)
    print(sum(lst), minN)