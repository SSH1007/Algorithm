import sys
input = lambda: sys.stdin.readline().rstrip()


dic = {'P': set(), 'K': set(), 'H': set(), 'T': set()}
S = input()
for i in range(0, len(S), 3):
    dic[S[i]].add(S[i+1:i+3])
P, K, H, T = map(len, dic.values())
if P+K+H+T != len(S)//3:
    print('GRESKA')
else:
    print(13-P, 13-K, 13-H, 13-T)