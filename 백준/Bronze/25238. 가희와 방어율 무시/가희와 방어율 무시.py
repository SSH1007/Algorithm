a, b = map(int, input().split())
result = a*(100-b)//100
print(1 if result<100 else 0)