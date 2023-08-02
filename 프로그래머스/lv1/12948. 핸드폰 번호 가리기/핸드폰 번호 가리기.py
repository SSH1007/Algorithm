def solution(phone_number):
    answer = ''
    l = len(phone_number)
    answer = '*'*(l-4)
    answer += phone_number[l-4:]
        
    return answer