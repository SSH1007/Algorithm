L = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
n = int(input())
s, e = 0, 0
if n in numbers:
    print(0)
else:
    numbers = [0]+numbers
    for i in range(1+L):
        if numbers[i] > n:
            e = numbers[i]
            s = numbers[i-1]+1
            break

    dap = 0
    for i in range(s, n+1):
        for j in range(n, e):
            if i < j:
                dap += 1
    print(dap)