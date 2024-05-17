N = int(input())
if N == 0:
    print(0)
    exit(0)
dap = ''
while N != 0:
    if N%-2 == 0:   #짝수
        dap = '0'+dap
        N = N//-2
    else:
        dap = '1'+dap
        N = N//-2+1
print(dap)