# 파일의 개수 N개(N<=50)
N = int(input())
# 사용한 클러스터 수 초기화
dap = 0
# N개의 파일들의 용량
files = list(map(int, input().split()))
# 클러스트의 크기 입력
size = int(input())
# 파일 개수만큼 순회
for n in range(N):
    # 크기가 0인 파일은 클러스터가 필요없다(무시)
    if files[n]==0:
        continue
    # 파일의 크기를 클러스트의 크기로 나눈 값의 올림 값만큼 클러스트의 수를 더한다.
    dap += (files[n]//size+1 if files[n]/size>files[n]//size else files[n]//size)
# 클러스터의 수와 기본 사이즈를 곱해 전체 클러스터의 크기 출력
print(dap*size)