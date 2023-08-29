import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    recruit = []
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        recruit.append((a, b))
    # 일단 서류심사 성적 순으로 정렬
    recruit.sort()
    # 서류 심사 1등은 무조건 뽑는다.
    newbie = 1
    # 면접 성적을 갱신하면서 선발할 수 있는 인원 카운트
    interviewScore = recruit[0][1]
    for i in range(1, N):
        if interviewScore > recruit[i][1]:
            interviewScore = recruit[i][1]
            newbie += 1
    print(newbie)