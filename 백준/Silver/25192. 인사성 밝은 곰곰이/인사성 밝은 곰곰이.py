import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
dic = dict()
for _ in range(N):
    chat = input().rstrip()
    if chat == 'ENTER':
        dic = dict()
    elif chat not in dic:
        dic[chat] = 1
        dap += 1
print(dap)