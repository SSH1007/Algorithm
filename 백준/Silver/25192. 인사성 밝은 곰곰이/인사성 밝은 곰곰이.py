N = int(input())
dap = 0
dic = dict()
for _ in range(N):
    chat = input()
    if chat == 'ENTER':
        dic = dict()
    else:
        if chat in dic:
            continue
        else:
            dic[chat] = 1
            dap += 1
print(dap)