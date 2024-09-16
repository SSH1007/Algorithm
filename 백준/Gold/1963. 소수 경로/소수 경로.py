import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    prime = [1]*10000
    prime[0], prime[1] = 0, 0
    for i in range(2, 100):
        if prime[i] == 1:
            for j in range(i+i, 10000, i):
                prime[j] = 0

    T = int(input())
    for _ in range(T):
        A, B = input().split()
        visited = [0]*10000
        visited[int(A)] = 1
        q = deque([(A, 0)])
        while q:
            cur, cnt = q.popleft()
            if cur == B:
                break
            for i in range(4):
                for j in range(10):
                    tmp = cur[:i]+str(j)+cur[i+1:]
                    if visited[int(tmp)] == 0 and int(tmp) > 999 and prime[int(tmp)] == 1:
                        q.append((tmp, cnt+1))
                        visited[int(tmp)] = visited[int(cur)] + 1
        print(visited[int(B)]-1)


if __name__ == '__main__':
    main()