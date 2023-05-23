import sys
input = sys.stdin.readline
from itertools import combinations_with_replacement
n = int(input().rstrip())
# 자연수를 넷 혹은 그 이하의 제곱수 합으로 나타내자
jegobs = [i*i for i in range(1, int(n**0.5)+1)]
jegobhabs = [sum(i) for i in combinations_with_replacement(jegobs, 2)]
jegobhabhabs = [sum(i) for i in combinations_with_replacement(jegobs, 3)]
if n in jegobs:
    print(1)
elif n in jegobhabs:
    print(2)
elif n in jegobhabhabs:
    print(3)
else:
    print(4)