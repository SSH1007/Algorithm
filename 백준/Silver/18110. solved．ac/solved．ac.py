import sys
input = sys.stdin.readline

# 소수부분이 0.5 이상이면 반올림
def customRound(n):
    return int(n)+1 if n-int(n)>=0.5 else int(n)

# n이 0이냐 아니냐로 분기
n = int(input().rstrip())
if n:
    # 데이터 받기
    lst = []
    for _ in range(n):
        lst.append(int(input().rstrip()))
    lst.sort()

    # 핵심 로직
    cnt = customRound(n*0.15)
    motherCnt = n-(2*cnt)
    motherlst = lst[cnt:-cnt] if cnt else lst
    dap = sum(motherlst)/motherCnt
    print(customRound(dap))
else:
    print(0)