import sys
input = sys.stdin.readline
N = int(input().rstrip())
for n in range(1, N+1):
    if n!=1:
        print()
    S = input().rstrip()
    dap = ''
    for s in S:
        if s=='Z':
            dap+='A'
        else:
            dap+=chr((ord(s)+1))
    print(f'String #{n}')
    print(dap)