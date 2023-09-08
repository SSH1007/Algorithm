HIARC = [0]*5
N = int(input())
S = input()
for s in S:
    if s == 'H':
        HIARC[0] += 1
    elif s == 'I':
        HIARC[1] += 1
    elif s == 'A':
        HIARC[2] += 1
    elif s == 'R':
        HIARC[3] += 1
    elif s == 'C':
        HIARC[4] += 1
print(min(HIARC))