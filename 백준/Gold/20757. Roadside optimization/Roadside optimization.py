import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX != rootY:
        # parent[x] 값이 음수면 x는 부모 노드로, abs(parent[x])만큼의 식구를 갖음
        # parent[x] 값이 양수면 x는 자식 노드로 parent[x]가 x의 부모임
        if parent[rootX] > parent[rootY]:
            parent[rootY] += parent[rootX]
            parent[rootX] = rootY
        else:
            parent[rootX] += parent[rootY]
            parent[rootY] = rootX


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        parent = [-1 for _ in range(N)]
        info = [list(map(int, input().split())) for _ in range(N)]
        for r in range(N):
            for c in range(N):
                if r!=c:
                    if info[r][c]:
                        union(parent, r, c)
        dap = 0
        for p in parent:
            if p < 0:
                dap += (abs(p)-1)
        print(dap)

        
if __name__ == '__main__':
    main()