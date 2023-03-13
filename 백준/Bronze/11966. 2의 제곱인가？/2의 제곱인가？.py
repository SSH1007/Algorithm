# 11966. 2의 제곱인가?

# 자연수 N 입력
N = int(input())
# N이 2^30까지이므로 그냥 0~30까지의 2의 제곱수들을 리스트에 담고
lst = [2**i for i in range(31)]
# 그 안에 N이 들어있는지 판단하면 끝
print(1 if N in lst else 0)