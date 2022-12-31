# 문장의 수 N 입력
N = int(input())
# N번 순회
for _ in range(N):
    setence = list(input().split())
    a = ' '.join(setence[:2])
    b = ' '.join(setence[2:])
    print(b,a)