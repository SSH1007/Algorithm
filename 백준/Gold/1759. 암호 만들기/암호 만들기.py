import sys
input = sys.stdin.readline


def main():
    L, C = map(int, input().rstrip().split())
    Cs = sorted(list(input().rstrip().split()))

    def check(c_lst):
        m = {'a', 'e', 'i', 'o', 'u'}
        m_cnt, j_cnt = 0, 0
        for l in c_lst:
            if l in m:
                m_cnt += 1
            else:
                j_cnt += 1
        if m_cnt >= 1 and j_cnt >= 2:
            return True
        else:
            return False

    lst = []
    visited = [0]*C

    def DFS(idx, length):
        if length == L:
            if check(lst):
                print(''.join(lst))
            return
        for c in range(idx, C):
            if not visited[c]:
                visited[c] = 1
                lst.append(Cs[c])
                DFS(c, length+1)
                visited[c] = 0
                lst.pop()
    DFS(0, 0)
    return


if __name__ == '__main__':
    main()