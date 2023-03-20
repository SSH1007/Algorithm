T = int(input())
for _ in range(T):
    HP, MP, ATK, DEF, h, m, a, d = map(int, input().split())
    BP = 1*((HP+h if HP+h>1 else 1)) + 5*((MP+m if MP+m>1 else 1)) + 2*((ATK+a if ATK+a>0 else 0)) + 2*(DEF+d)
    print(BP)