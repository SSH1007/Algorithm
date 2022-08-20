min = list(map(int, input().split()))
man = list(map(int, input().split()))
print(sum(min) if sum(min)==sum(man) else max(sum(min),sum(man)))