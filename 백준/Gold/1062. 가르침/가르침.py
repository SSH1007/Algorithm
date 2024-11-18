import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations as comb


def main():
    N, K = map(int, input().split())
    # anta*tica이므로 a, n, t, i, c는 필수 (5개)
    if K < 5:
        print(0)
        exit(0)
    d_set = {'a', 'c', 'i', 'n', 't'}
    new_set = set()
    dic = dict()
    lst = []
    for _ in range(N):
        S = set(input()[4:-4])
        S = S-d_set     # 차집합
        new_set.update(S)
        lst.append(S)
    # 기존 5개 외의 문자들을 충분히 가르칠 수 있으면 전부 가능
    if len(new_set) <= K-5:
        print(N)
        exit(0)
    C = comb(new_set, K-5)
    ans = 0
    for c in C:
        c = set(c)
        dap = 0
        for l in lst:
            if len(l-c) == 0:
               dap += 1
        if ans < dap:
            ans = dap
    print(ans)


if __name__ == '__main__':
    main()