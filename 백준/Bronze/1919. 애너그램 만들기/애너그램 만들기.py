# 두 문장에서 공통된 것 이외를 계속 지워나가면된다
A = list(input())
B = list(input())
cnt = 0
i = 0
while i<len(A):
    if A[i] in B:
        B.pop(B.index(A[i]))
        A.pop(i)
        i-=1
    i+=1
print(len(A)+len(B))