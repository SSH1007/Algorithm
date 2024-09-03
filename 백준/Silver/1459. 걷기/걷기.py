import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X, Y, W, S = map(int, input().split())
    # 대각선 이동보다 십자이동 2번이 효율적일때
    if W*2 <= S:
        print((X+Y)*W)
        return
    # 대각선 이동이 십자이동 2번보다 효율적일때
    move = min(X, Y)*S
    left = max(X, Y) - min(X, Y)  # left는 일직선임

    if left == 1:
        print(move+W)
    else:
        # 대각선 이동 2 vs 십자 이동 2
        if W*2 > S*2:
            if left%2:
                move += left*S
                move -= S
                move += W
            else:
                move += left*S
        else:
            move += left*W
        print(move)


if __name__ == '__main__':
    main()