def solution(nums):
    dic = dict()
    for n in nums:
        if n not in dic:
            dic[n] = 1
        else:
            dic[n] += 1
    answer = min(len(nums)//2, len(dic))
    return answer