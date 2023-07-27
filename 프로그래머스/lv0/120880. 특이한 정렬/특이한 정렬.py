def solution(numlist, n):
    answer = []
    lst = []
    for num in numlist:
        lst.append((num, abs(num-n)))
    lst.sort(key=lambda x:(x[1], -x[0]))
    for l in lst:
        answer.append(l[0])
    return answer