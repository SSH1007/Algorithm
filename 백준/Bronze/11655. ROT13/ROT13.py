import sys
input = sys.stdin.readline
S = input().rstrip()
dap = []
for s in S:
    if 65<=ord(s)<=90:
        dap.append(chr((ord(s)+13)%90+64) if ord(s)+13 > 90 else chr(ord(s)+13))
    elif 97<=ord(s)<=122:
        dap.append(chr((ord(s)+13)%122+96) if ord(s)+13 > 122 else chr(ord(s)+13))
    else:
        dap.append(s)
print(*dap, sep='')