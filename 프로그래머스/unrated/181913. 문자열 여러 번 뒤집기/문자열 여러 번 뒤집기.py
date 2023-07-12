def solution(my_string, queries):
    answer = ''
    for q in queries:
        A = my_string[:q[0]]
        B = my_string[q[0]:q[1]+1]
        newB = B[::-1]
        C = my_string[q[1]+1:]
        my_string = A+newB+C
    answer = my_string
    return answer