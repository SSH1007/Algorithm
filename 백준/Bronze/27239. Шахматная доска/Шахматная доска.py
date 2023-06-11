import sys
input = sys.stdin.readline
n = int(input().rstrip())
dic = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 0:'h'}
a, b = 0, 0
a = dic[n%8]
if (n/8)%1:
    b = n//8+1
else:
    b = n//8

print(a,b, sep='')