def solution(emergency):
    answer = []
    lst = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(lst.index(e)+1)
    return answer