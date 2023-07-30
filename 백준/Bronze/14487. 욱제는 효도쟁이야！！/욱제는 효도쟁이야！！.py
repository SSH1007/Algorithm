import sys
input = sys.stdin.readline
n = int(input().rstrip())
towns = list(map(int, input().rstrip().split()))
towns.sort()
print(sum(towns[:-1]))