N, M = map(int, input().split())
A, B = input().split()
dic = {'A': 3, 'B': 2, 'C': 1, 'D': 2, 'E': 4, 'F': 3, 'G': 1, 'H': 3,
       'I': 1, 'J': 1, 'K': 3, 'L': 1, 'M': 3, 'N': 2, 'O': 1, 'P': 2,
       'Q': 2, 'R': 2, 'S': 1, 'T': 2, 'U': 1, 'V': 1, 'W': 1, 'X': 2,
       'Y': 2, 'Z': 1}
idle = ''
idx = 0
for i in range(min(N, M)):
    idle += A[i]
    idle += B[i]
    idx = i
idle += A[idx+1:]
idle += B[idx+1:]

match = []
for i in idle:
    match.append(dic[i])
while 1:
    if len(match) == 2:
        break
    tmp = []
    for i in range(len(match)-1):
        tmp.append((match[i]+match[i+1]) % 10)
    match = tmp
print(int(''.join(map(str, match))), '%', sep='')