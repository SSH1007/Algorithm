# 기타에서 N개의 줄이 끊어졌다.
# 기타줄 브랜드 M개에서 기타 줄을 사자!
# M개의 브랜드에서 6개 패키지와 낱개를 골라, 가장 싸게 N개를 살 수 있도록 하자
N, M = map(int, input().split())
# 출력할 답인 최솟값 초기화
dap = 0
# 패키지 가격, 낱개 가격 초기화
packageM, singleM = 1000, 1000
# 브랜드 수 M개만큼 반복
for _ in range(M):
    # 각 브랜드의 패키지 가격과 낱개 가격을 받고, 가장 싼 가격들을 고른다.
    a, b = map(int, input().split())
    if packageM > a:
        packageM = a
    if singleM > b:
        singleM = b
# 패키지나 낱개가 만약 0원이면
if packageM == 0 or singleM == 0:
    # 전부 공짜로 사지
    print(0)
else:
    # 낱개가 몇 개 있어야 패키지 가격과 동일한가?
    c = int(packageM/singleM)
    # 낱개가 6개 이하만 있어도 패키지와 동일한 가격이라면
    if c >= 6:
        # 낱개로만 사도 OK
        print(singleM*N)
    # 아니면
    else:
        # 패키지로 사고 난 뒤, 나머지도 패키지가 싸게 먹히면
        if N%6 > c:
            print((N//6+1)*packageM)
        # 패키지로 사고 난 뒤, 낱개로 사는게 싸게 먹히면
        else:
            print((N//6)*packageM + (N%6)*singleM)