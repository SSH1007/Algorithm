def solution(arr):
    answer = []
    i = 0
    while 1:
        if i >= len(arr):
            break
        if not answer:
            answer.append(arr[i])
        elif answer and answer[-1] == arr[i]:
            answer.pop()
        elif answer and answer[-1] != arr[i]:
            answer.append(arr[i])
        i += 1
    if not answer:
        answer.append(-1)
    return answer