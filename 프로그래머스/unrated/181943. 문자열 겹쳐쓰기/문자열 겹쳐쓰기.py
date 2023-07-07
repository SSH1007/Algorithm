def solution(my_string, overwrite_string, s):
    answer = ''
    s = int(s)
    f = my_string[:s]
    e = my_string[s+len(overwrite_string):]
    answer = f+overwrite_string+e
    return answer