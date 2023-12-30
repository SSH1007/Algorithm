L = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
n = int(input())
s, e = 1, 1
for number in numbers:
    if number > n:
        e = number-1
        break
    if number < n:
        s = number+1
    if number == n:
        break

dap = 0
for i in range(s, e+1):
    for j in range(i+1, e+1):
        if i > n or j < n:
            continue
        dap += 1
print(dap)