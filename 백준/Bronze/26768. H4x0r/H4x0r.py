import sys
input = sys.stdin.readline
dic = {'a':'4', 'e':'3', 'i':'1', 'o':'0', 's':'5' }
S = input().rstrip()
dap  = []
for s in S:
    if s in dic:
        dap.append(dic[s])
    else:
        dap.append(s)
print(''.join(dap))