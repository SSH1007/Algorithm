import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import permutations


def main():
    yumi = list(map(int, input().split()))
    lst = [list(map(int, input().split())) for _ in range(3)]
    perm = permutations(lst)
    dap = float('inf')
    for p in perm:
        tmp = ((p[0][0]-yumi[0])**2+(p[0][1]-yumi[1])**2)**0.5
        for i in range(2):
            x = p[i+1][0]-p[i][0]
            y = p[i+1][1]-p[i][1]
            tmp += (x**2+y**2)**0.5
        dap = min(dap, tmp)
    print(int(dap))


if __name__ == '__main__':
    main()