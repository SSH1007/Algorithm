numbers = list(map(int, input().split()))
a = numbers.pop(numbers.index(min(numbers)))
b = numbers.pop(numbers.index(max(numbers)))
print(abs((a+b)-sum(numbers)))