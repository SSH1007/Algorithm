def solution(num_list):
    answer = 0
    gob, hap = 1, 0
    hap = sum(num_list)
    for n in num_list:
        gob*=n
    if gob < hap**2:
        answer = 1
    return answer