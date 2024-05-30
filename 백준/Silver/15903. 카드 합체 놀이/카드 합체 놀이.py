import sys
input = sys.stdin.readline
# 카드의 개수 n(<=1000), 합체 수 m(<=15000)
n, m = map(int, input().rstrip().split())
# 맨 처음 카드의 상태
As = sorted(list(map(int, input().rstrip().split())))
# 목표 : m번의 합체를 모두 끝낸 뒤, 모든 카드의 수를 더한 값이 최소값이 되어야 한다.

for _ in range(m):
    As[0], As[1] = As[0]+As[1], As[0]+As[1]
    As.sort()
print(sum(As))