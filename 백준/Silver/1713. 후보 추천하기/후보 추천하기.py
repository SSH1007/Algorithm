import sys
input = sys.stdin.readline


def main():
    # 사진틀의 개수 N
    N = int(input().rstrip())
    # 전체 학생의 총 추천 횟수 M
    M = int(input().rstrip())
    # 추천받은 학생의 번호 목록
    std = list(map(int, input().rstrip().split()))
    # 사진틀에 실린 학생 목록
    std_lst = []
    # 실린 학생들의 추천받은 횟수
    rcm_cnt = []
    for n in range(M):
        if std[n] in std_lst:
            rcm_cnt[std_lst.index(std[n])] += 1
        else:
            if len(std_lst) >= N:
                for i in range(len(std_lst)):
                    if rcm_cnt[i] == min(rcm_cnt):
                        del std_lst[i]
                        del rcm_cnt[i]
                        break
            std_lst.append(std[n])
            rcm_cnt.append(1)
    print(*sorted(std_lst))


if __name__ == '__main__':
    main()