def quick(array):
    if len(array) <= 1:
        return array
    pivot, tail = array[0], array[1:]
    left = [x for x in tail if x > pivot]
    right = [x for x in tail if x <= pivot]
    return quick(left) + [pivot] + quick(right)

        
def solution(s):
    answer = ''
    S = list(s)
    dap = quick(S)
    answer = ''.join(dap)
    return answer