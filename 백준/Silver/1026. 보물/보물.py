# B 배열은 정렬하면 안된다는 조건이 붙어있음
# 길이 N 받음
N = int(input())
# 정수 배열 A
A = list(map(int, input().split()))
# 정수 배열 B
B = list(map(int, input().split()))
# A와 B의 원소의 곱을 담을 빈 리스트 생성
dap = []
# A가 빌 때까지 반복
while A:
    # A의 가장 큰 놈을 pop
    a = A.pop(A.index(max(A)))
    # B의 가장 작은 놈을 pop
    b = B.pop(B.index(min(B)))
    # pop한 놈들을 곱한 값을 dap 리스트에 넣는다
    dap.append(a*b)
# dap 리스트의 원소의 합을 출력
print(sum(dap))