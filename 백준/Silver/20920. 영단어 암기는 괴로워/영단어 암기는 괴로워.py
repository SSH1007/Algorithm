import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
dic = {}
for _ in range(N):
    word = input().rstrip()
    l = len(word)
    if l >= M:
        if not word in dic:
            dic[word] = 1
        else:
            dic[word] += 1
dap = sorted(dic.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
for d in dap:
    print(d[0])