n = int(input())
for _ in range(n):
    # x는 좀비가 먹은 뇌의 수, y는 좀비가 살아가기 위해 필요한 뇌의 수
    x,y= map(int, input().split())
    if x>=y:
        print('MMM BRAINS')
    else:
        print('NO BRAINS')