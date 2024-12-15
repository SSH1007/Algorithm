import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
lst = []
s = set()
for _ in range(N):
    k = ' ' + input()
    hot_key = ''
    flag = True
    for i in range(1, len(k)):
        if k[i] != ' ' and not k[i].lower() in s and k[i-1] == ' ' and flag:
            s.add(k[i].lower())
            hot_key += '['+k[i]+']'
            flag = False
        else:
            hot_key += k[i]
    if flag:
        hot_key = ''
        for i in range(1, len(k)):
            if k[i] != ' ' and not k[i].lower() in s and flag:
                s.add(k[i].lower())
                hot_key += '['+k[i]+']'
                flag = False
            else:
                hot_key += k[i]
    print(hot_key)