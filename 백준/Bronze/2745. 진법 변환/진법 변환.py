N, B = input().split()
B = int(B)
dap = 0
for n in range(len(N)):
    if N[n].isdigit():
        dap+=(int(N[n])*(B**(len(N)-n-1)))
    else:
        dap+=((ord(N[n])-55)*(B**(len(N)-n-1)))
print(dap)