N = int(input())
tower = [0]*10
tower[1] = 1
for n in range(2, N):
    tower[n] = tower[n-1] + n
print(tower[N-1])