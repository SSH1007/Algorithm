import sys
input = sys.stdin.readline
dic = dict()
tree = 0
while 1:
    name = input().rstrip()
    if not name:
        break
    if not name in dic:
        dic[name] = 1
    else:
        dic[name] += 1
    tree += 1

lst = sorted(dic.items())
for l in lst:
    print("%s %.4f" % (l[0], l[1]/tree*100))