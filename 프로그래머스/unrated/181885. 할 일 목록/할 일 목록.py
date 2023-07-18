def solution(todo_list, finished):
    answer = []
    for f in range(len(finished)):
        if not finished[f]:
            answer.append(todo_list[f])
    return answer