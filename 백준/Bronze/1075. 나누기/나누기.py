arr = []
N = input()
F = int(input())
N1 = int(N[:-2])*100

N2 = int(N[-2:])
for i in range(N2,100):
    if (N1+(i%100))%F == 0:
        arr.append((N1+(i%100))%100)

N2 = int(N[-2:])
for i in range(0, N2):
    if (N1+(i%100))%F == 0:
        arr.append((N1+(i%100))%100)

print('0'+str(min(arr)) if len(str(min(arr)))<2 else min(arr))