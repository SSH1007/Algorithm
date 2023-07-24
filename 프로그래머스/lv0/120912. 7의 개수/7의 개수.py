def solution(array):
    answer = 0
    s = ''
    for a in array:
        s += str(a)
    answer = s.count('7')
    return answer