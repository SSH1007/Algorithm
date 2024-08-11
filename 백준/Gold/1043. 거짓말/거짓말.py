import sys
input = lambda: sys.stdin.readline().rstrip()


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, rank, x, y, know):
    rootX = find(parent, x)
    rootY = find(parent, y)
    if rootX in know and rootY in know:
        return
    if rootX in know:
        parent[rootY] = rootX
    elif rootY in know:
        parent[rootX] = rootY
    else:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1


def main():
    N, M = map(int, input().split())

    parent = [i for i in range(N+1)]
    rank = [0]*(N+1)
    truth = list(map(int, input().split()))
    # 진실을 알고 있는 사람들
    s = set(truth[1:])

    dap = 0
    # PartyPeople
    PP_lst = []
    for _ in range(M):
        PP = list(map(int, input().split()))[1:]
        PP_lst.append(PP)
        for i in range(len(PP)-1):
            union(parent, rank, PP[i], PP[i+1], s)

    for pp in PP_lst:
        for p in pp:
            if find(parent, p) in s:
                break
        else:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()