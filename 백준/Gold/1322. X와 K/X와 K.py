import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    #   101
    #    1
    #  1 0
    #  1 1
    # 10 0
    # 10 1
    # print(int('10010',2))  # 5+18 == 5|18

    X, K = map(int, input().split())
    Y = 0
    bit_position = 0
    # bit_position을 계속 증가시키는 것으로
    # X의 탐색할 위치, Y에 더할 값을 찾는다.

    # 예) K가 101이면 10(1), 1(0), (1) 순으로 순회하며 탐색
    while K > 0:
        # 예) X가 101이면 10(1), 1(0)1, (1)01 순으로 순회
        # X의 현재 비트가 0이면
        if (X & (1 << bit_position)) == 0:
            # K의 가장 오른쪽 비트가 1이면
            if (K & 1) != 0:
                Y |= (1 << bit_position)  # Y의 해당 비트를 1로 설정
            K >>= 1  # K를 오른쪽으로 시프트하여 다음 비트를 확인
        bit_position += 1  # X의 다음 비트로 이동
    print(Y)


if __name__ == '__main__':
    main()