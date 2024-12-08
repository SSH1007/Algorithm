import sys
input = lambda: sys.stdin.readline().rstrip()
import re


def F(S):
    p = re.compile('[A-F]?A+F+C+[A-F]?')
    a = p.match(S)
    if a and a.end()==len(S):
        return 1
    else:
        return 0


T = int(input())
for _ in range(T):
    S = input()
    if F(S):
        print('Infected!')
    else:
        print('Good')