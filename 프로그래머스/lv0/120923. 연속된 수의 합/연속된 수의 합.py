def solution(num, total):
    
    middle = total // num
    answer =  [i for i in range(middle - (num-1)//2, middle + (num + 2)//2)]
    return answer