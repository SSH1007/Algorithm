# 6, 3, 0
def garo(b, idx):
    for i in range(idx, idx+3):
        b ^= (1<<i)
    return bin(b)[2:]


# 2 1 0
def sero(b, idx):
    for i in range(idx, idx+7, 3):
        b ^= (1<<i)
    return bin(b)[2:]


def cross1(b):  # \
    for i in [8,4,0]:
        b ^= (1<<i)
    return bin(b)[2:]


def cross2(b):  # /
    for i in [6,4,2]:
        b ^= (1<<i)
    return bin(b)[2:]


def BFS(b):
    visited = [0]*512
    visited[int(b, 2)] = 1
    q = deque([(int(b, 2), 0)])
    while q:
        pb, cnt = q.popleft()
        if pb == 511 or pb == 0:
            return cnt
        for i in [6, 3, 0]:
            nb = garo(pb, i)
            if not visited[int(nb, 2)]:
                q.append((int(nb, 2), cnt+1))
                visited[int(nb, 2)] = 1
        for i in [2, 1, 0]:
            nb = sero(pb, i)
            if not visited[int(nb, 2)]:
                q.append((int(nb, 2), cnt+1))
                visited[int(nb, 2)] = 1
        nb = cross1(pb)
        if not visited[int(nb, 2)]:
            q.append((int(nb, 2), cnt+1))
            visited[int(nb, 2)] = 1
        nb = cross2(pb)
        if not visited[int(nb, 2)]:
            q.append((int(nb, 2), cnt+1))
            visited[int(nb, 2)] = 1
    return -1


from collections import deque
T = int(input())
for _ in range(T):
    case = [input().split(' ') for _ in range(3)]
    b_case = ''.join([''.join(['1' if c == 'H' else '0' for c in ca]) for ca in case])

    print(BFS(b_case))