N, M = map(int, input().split())
dic = dict()
dic2 = dict()
for _ in range(N):
    team = input()
    if team not in dic:
        dic[team] = []
    cnt = int(input())
    for _ in range(cnt):
        name = input()
        dic[team].append(name)
        dic2[name] = team
    dic[team].sort()

for _ in range(M):
    name = input()
    quiz = int(input())
    if quiz == 0:
        for n in dic[name]:
            print(n)
    elif quiz == 1:
        print(dic2[name])