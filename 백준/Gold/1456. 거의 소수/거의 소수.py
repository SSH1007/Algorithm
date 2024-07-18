A, B = map(int, input().split())
# N제곱하는 것으로 '거의 소수'가 되는 소수의 최대값은 B의 제곱근이다
lst = [True] * (int(B**0.5)+1)
lst[0], lst[1] = False, False
for i in range(2, int(B**0.5)+1):
    if lst[i]:
        for j in range(i*i, int(B**0.5)+1, i):
            lst[j] = False

dap = 0

for i in range(len(lst)):
    # 소수가 아니다
    if lst[i] == False:
        continue

    tmp = i
    while tmp <= B:
        tmp *= i
        if A <= tmp <= B:
            dap += 1

print(dap)