import sys
input = sys.stdin.readline
while 1:
    case = input().rstrip()
    if case == '':
        break
    s, t = case.split()
    i = 0
    for S in s:
        if not S in t:
            print('No')
            break
        else:
            a = t[i:].find(S)
            if a == -1:
                print('No')
                break
            i = i+a+1
    else:
        print('Yes')