# 28018 누적합(imos법 기본문제)
import sys
input = sys.stdin.readline


def main():
    # 학생 수가 100,000명, 응답한 시각의 범위는 1~1,000,000이므로
    # 평소에 하던 대로 범위를 +1로 채운다면
    # 최악의 경우, 100,000 * 1,000,000번 작업해야한다. 
    # 따라서 imos법으로 시간복잡도를 줄인다!
    imos = [0]*1000002
    # ^ 종료 시각이 E+1이므로 시간 범위도 +1 증가
    N = int(input().rstrip())
    for _ in range(N):
        S, E = map(int, input().rstrip().split())
        # imos법: 각각의 입력에서 시작과 끝만 기록 후 나중에 한꺼번에 처리
        imos[S] += 1
        # 각 좌석은 사용이 종료되는 시각에 곧바로 선택될 수 없으므로,
        # 종료 시각 E보다 1이 지난 시각에 자리가 비게 되어 선택할 수 있게 된다.
        imos[E+1] -= 1
    now = 0
    for i in range(1, 1000001):
        now += imos[i]
        imos[i] = now
    Q = int(input().rstrip())
    Qs = list(map(int, input().rstrip().split()))
    for q in range(Q):
        print(imos[Qs[q]])


if __name__ == '__main__':
    main()