# 주사위 S1(2~20면), S2(2~20면), S3(2~40면)의 값을 받음
S1, S2, S3 = map(int, input().split())
# 합들을 담을 딕셔너리 생성
dic = dict()
# 20*20*40번 반복하면서 세 주사위의 합과 그 빈도를 딕셔너리에 담는다.
for i in range(1, S1+1):
    for j in range(1, S2+1):
        for k in range(1, S3+1):
            hap = i+j+k
            if hap in dic:
                dic[hap] += 1
            else:
                dic[hap] = 1
# 아이템을 리스트에 담고
lst = list(dic.items())
# 빈도의 최댓값을 변수에 담는다.
maxes= max(dic.values())
# 리스트를 빈도 수를 키로 하여 정렬
lst.sort(key = lambda x:x[1])
# 리스트를 순회하면서
for l in lst:
    # 빈도수가 최대인 제일 첫타자를
    if l[1] == maxes:
        # 출력하고 브레이크
        print(l[0])
        break