Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())
dap = 0
C=Cr-Ca
B=Br-Ba
P=Pr-Pa
if C>0:
    dap+=C
if B>0:
    dap+=B
if P>0:
    dap+=P
print(dap)