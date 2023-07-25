def solution(sides):
    answer = 0
    # sides 안에 이미 가장 긴 변이 있다면
    for _ in range(max(sides)-min(sides)+1, max(sides)+1):
        answer += 1
    # sides 안에 없다면
    for _ in range(max(sides)+1, max(sides)+min(sides)):
        answer += 1
    return answer