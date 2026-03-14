import sys
import re
S = sys.stdin.readlines()
flag = 1
while 1:
    tmp = []
    for s in S:
        a = re.sub('BUG', '', s).rstrip()
        tmp.append(a)
    for t in tmp:
        if 'BUG' in t:
            flag = 0
            break
    else:
        flag = 1
    S = tmp
    if flag:
        break
for t in tmp:
    print(t)