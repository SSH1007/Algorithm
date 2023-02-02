A, B, C = map(int, input().split())
dap = 0
while 1:
    if abs(A-B)==abs(B-C)==1:
        break
    if abs(A-B) <= abs(B-C):
        A=B
        B=B+1
    else:
        C=B
        B=B-1
    dap+=1        
print(dap)