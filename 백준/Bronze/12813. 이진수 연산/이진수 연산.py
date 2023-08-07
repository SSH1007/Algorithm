import sys
input = sys.stdin.readline
A = input().rstrip()
B = input().rstrip()
dap = ''
for n in range(len(A)):
    if A[n] == '1' and A[n] == B[n]:
        dap += '1'
    else:
        dap += '0'
print(dap)
dap = ''
for n in range(len(A)):
    if A[n]=='1' or B[n] == '1':
        dap += '1'
    else:
        dap += '0'
print(dap)
dap = ''
for n in range(len(A)):
    if A[n] == B[n]:
        dap += '0'
    else:
        dap += '1'
print(dap)
dap = ''
for n in range(len(A)):
    if A[n] == '0':
        dap += '1'
    else:
        dap += '0'
print(dap)
dap = ''
for n in range(len(A)):
    if B[n] == '0':
        dap += '1'
    else:
        dap += '0'
print(dap)