def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for s in str(n):
        answer+=int(s)

    return answer