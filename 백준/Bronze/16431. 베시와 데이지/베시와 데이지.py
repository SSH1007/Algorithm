import sys
input = sys.stdin.readline
Br, Bc = map(int, input().rstrip().split())
Dr, Dc = map(int, input().rstrip().split())
Jr, Jc = map(int, input().rstrip().split())
                
# Daisy : John과의 거리 x,y의 합
# Bessie : John과의 거리 x,y 중 최대값
Dd = sum([abs(Jr-Dr), abs(Jc-Dc)])
Bd = max(abs(Jr-Br), abs(Jc-Bc))

if Bd<Dd:
    print('bessie')
elif Bd>Dd:
    print('daisy')
else:
    print('tie')