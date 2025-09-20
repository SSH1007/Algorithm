import sys
input = lambda: sys.stdin.readline().rstrip()


def rec(i, tree, N):
    if i > N//2:
        return tree[i]
    left = rec(2*i, tree, N)
    right = rec(2*i+1, tree, N)
    tmp = min(left, right)
    tree[i*2] -= tmp
    tree[i*2+1] -= tmp
    tree[i] += tmp
    return tmp


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        tree = [0]*N
        As = list(map(int, input().split()))
        for i in range(N//2+1):
            tree[N//2+i] = As[i]
        tree = [0] + tree
        rec(1, tree, N)
        print(sum(tree))


if __name__ == '__main__':
    main()