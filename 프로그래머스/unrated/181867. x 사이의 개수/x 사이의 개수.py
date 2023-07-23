def solution(myString):
    answer = []
    lst = list(myString.split('x'))
    print(lst)
    for l in lst:
        answer.append(len(l)) 
    return answer