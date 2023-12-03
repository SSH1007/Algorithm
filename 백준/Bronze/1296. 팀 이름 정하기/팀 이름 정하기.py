yeondu = input()
N = int(input())
lst = []
for _ in range(N):
    team = input()
    L = (yeondu.count('L')+team.count('L'))
    O = (yeondu.count('O')+team.count('O'))
    V = (yeondu.count('V')+team.count('V'))
    E = (yeondu.count('E')+team.count('E'))
    possibility = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100
    lst.append((team, possibility))
lst.sort(key=lambda x:(-x[1], x[0]))
print(lst[0][0])