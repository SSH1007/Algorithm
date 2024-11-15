K = int(input())
bK = bin(K)[2:]
end = 0
for i in range(1, len(bK)):
    if bK[i] == '1':
        end = i
if end:
    print(2**len(bK), end+1)
else:
    print(int(bK, 2), 0)