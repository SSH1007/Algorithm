N=int(input())
S=input()
hasi=0
for index,s in enumerate(S):
    hasi+=(ord(s.upper())-64)*(31**index)
print(hasi%1234567891)