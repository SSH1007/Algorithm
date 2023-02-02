A, B, C = map(int, input().split())
print(max(abs(A-B),abs(B-C))-1)