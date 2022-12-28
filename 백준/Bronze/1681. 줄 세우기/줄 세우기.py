# 학생 수 기준 N과 라벨에 포함되지 않아야 하는 수 L 입력
N, L = map(int, input().split())
# N명에 도달했는지 세는 수 cnt
cnt = 0
# 라벨 숫자
number = 0
# cnt가 N이 될 때까지 반복
while cnt != N:
    # 라벨 숫자 += 1 
    number+=1
    # 숫자 L이 라벨 숫자에 포함되지 않으면
    if str(L) not in str(number):
        # cnt+=1
        cnt+=1
print(number)    