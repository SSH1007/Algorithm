# 유니온 파인드 : 합집합 찿기 or 서로소 집합 찾기
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    parent = [-1 for _ in range(n+1)]
    # parent[i] 값이 양수: i는 자식 노드로, i의 부모 노드는 parent[i]
    # parent[i] 값이 음수: i는 부모 노드로, 자기 자신을 포함해
    #   parent[i]의 절대값만큼의 크기를 갖고 있다.
    #   예) parent[1] = -3이면 부모 1, 자식 x, y의 트리 구성

    def find(x):
        # 부모 노드라면 값 호출
        if parent[x] < 0:
            return x
        # 부모 노드를 찾을 때까지 재귀적 호출
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        # parent[x] 양수 : x는 자식 노드
        # parent[x] 음수 : x는 부모 노드
        # 트리가 점점 깊어지지 않도록 트리의 높이가 낮은 트리가
        # 높이가 높은 트리 밑으로 들어가야 한다.
        # 양 > 양 : 부모 노드 이름끼리의 비교이므로 그냥 하던대로
        # 양 > 음 : 부모(음수) 아래로 자식(양수)이 들어간다
        # 음 > 음 : 부모(더 작은 음수, -1) 아래로 자식(더 큰 음수, -7)이 들어간다.
        if parent[x] > parent[y]:
            parent[y] += parent[x]
            parent[x] = y
        else:
            parent[x] += parent[y]
            parent[y] = x

    def isUnion(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return True
        return False

    for _ in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            union(a, b)
        else:
            if isUnion(a, b):
                print('YES')
            else:
                print('NO')


if __name__ == '__main__':
    main()