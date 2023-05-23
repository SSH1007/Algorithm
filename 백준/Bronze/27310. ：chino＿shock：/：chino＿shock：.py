import sys
input = sys.stdin.readline

N = input().rstrip()
# A=이모지의 전체 길이, B=콜론의 개수, C=언더바의 개수
A, B, C = 0, 0, 0
A = len(N)
for a in range(A):
    if N[a] == ':':
        B+=1
    if N[a] == '_':
        C+=1
print(A+B+(C*5))