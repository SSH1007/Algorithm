import sys
input = sys.stdin.readline
msg = input()
a = msg.count(':-)')
b = msg.count(':-(')
if a==0 and b==0:
    print('none')
elif a==b:
    print('unsure')
elif a>b:
    print('happy')
elif a<b:
    print('sad')