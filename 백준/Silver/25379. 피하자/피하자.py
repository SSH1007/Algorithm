import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    # 2로 나눈 나머지로만 보면 본 문제는 0, 1로 구성된 배열을
    # 내림차순, 혹은 오름차순으로 만드는 문제
    As = [l%2 for l in list(map(int, input().split()))]
    dap = int(1e9)
    for i in range(2):
        cnt, acc = 0, 0
        for j in range(N):
            if As[j] == i:
                acc += 1
            else:
                cnt += acc
        dap = min(dap, cnt)
    print(dap)


if __name__ == '__main__':
    main()