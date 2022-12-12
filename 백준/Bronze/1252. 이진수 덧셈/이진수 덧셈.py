# 두 개의 이진수를 string 형태로 받는다.
a, b = input().split()
# 변수 dap에 이진수들을 십진수로 바꿔 더한다. 
dap = int(a,2) + int(b,2)
# 더한 값을 이진수로 바꿔 출력한다.(앞의 0b는 제외하고)
print(bin(dap)[2:])