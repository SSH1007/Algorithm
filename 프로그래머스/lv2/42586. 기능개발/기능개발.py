from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    progress = deque(progresses)
    speed = deque(speeds)
    tmp = 0
    dic = dict()
    while progress:
        p = progress.popleft()
        s = speed.popleft()
        day = math.ceil((100-p)/s)
        tmp = max(tmp, day)
        if tmp>=day:
            if tmp not in dic:
                dic[tmp] = 1
            else:
                dic[tmp] +=1
    answer = list(dic.values())
    return answer