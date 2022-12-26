# 숫자 N을 받는다.
N = int(input())
# 1부터 N까지의 수를 이어 새로운 하나의 수 생성
newN = ''.join(map(str, range(1,N+1)))
# find 함수로 N을 찾아서 가장 먼저 등장하는 위치 출력
print(newN.index(str(N))+1)