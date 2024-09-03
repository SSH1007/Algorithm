import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    # 2로 나눈 나머지로만 보면 본 문제는 0, 1로 구성된 배열을
    # 내림차순, 혹은 오름차순으로 만드는 문제
    As = [l%2 for l in list(map(int, input().split()))]

    # 지금까지 등장한 홀/짝수의 개수
    odd_cnt = 0
    even_cnt = 0
    # 홀/짝수를 왼쪽으로 몰아넣기 위한 총 이동 횟수
    left_odd = 0
    left_even = 0

    for n in range(N):
        if As[n] == 0:
            even_cnt += 1
            left_odd += odd_cnt
        else:
            odd_cnt += 1
            left_even += even_cnt
    print(min(left_odd, left_even))


if __name__ == '__main__':
    main()