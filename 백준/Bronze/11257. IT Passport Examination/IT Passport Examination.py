# 전략 35점
# 경영 25점
# 기술 40점
# 총점 55점 이상이고,
# 각 분야마다 30% 이상일 경우 PASS, 아니면 FAIL
N = int(input())
for _ in range(N):
    lst = list(map(int, input().split()))
    hap = sum((lst[1], lst[2], lst[3]))
    if lst[1]>=(35*0.3) and lst[2]>=(25*0.3) and lst[3]>=(40*0.3) and hap>=55:
        print(lst[0], hap, 'PASS')
    else:
        print(lst[0], hap, 'FAIL')