import sys
input = sys.stdin.readline
N = int(input())
lst = []
for idx,n in enumerate(range(N),start=1):
    ip = input().rstrip()
    lst.append(f'{idx}. {ip}')
for l in lst:
    print(l)