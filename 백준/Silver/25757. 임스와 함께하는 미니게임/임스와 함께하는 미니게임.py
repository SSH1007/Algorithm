dic = {'Y': 2, 'F' : 3, 'O' : 4}
N, G = input().split()
s = set()
for _ in range(int(N)):
    s.add(input())
print(len(s)//(dic[G]-1))