def solution(rsp):
    answer = ''
    dic = {'2':'0', '0':'5', '5':'2'}
    for h in rsp:
        answer += dic[h]
    return answer