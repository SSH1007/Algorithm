import sys
input = sys.stdin.readline
n = int(input().rstrip())
dan = input().rstrip()+'d'
lst = []
tmp = ''
for d in dan:
    if d.isdigit():
        tmp += d
    else:
        if tmp != '':
            lst.append(int(tmp))
            tmp = ''
print(sum(lst))