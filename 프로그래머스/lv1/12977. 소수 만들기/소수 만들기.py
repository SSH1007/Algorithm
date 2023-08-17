def solution(nums):
    answer = 0
    
    sosu = [0]*3001
    for s in range(2, int(3000**0.5)+1):
        if not sosu[0]:
            for ss in range(s+s, 3001, s):
                sosu[ss] = 1
    # print(sosu)
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                if not sosu[nums[i]+nums[j]+nums[k]]:
                    answer += 1

    return answer