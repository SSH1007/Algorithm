import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dic = dict()
for _ in range(N):
    dango = input()[::-1]
    for i in range(len(dango)):
        if not dango[i] in dic:
            dic[dango[i]] = 10**i
        else:
            dic[dango[i]] += 10**i

items = sorted(dic.values(), reverse=True)
dap = 0
for i in range(len(items)):
    dap += items[i]*(9-i)
print(dap)