def solution(num_list):
    a = sum(num_list)
    b = 1
    for n in num_list:
        b *= n
    if a**2 > b:
        return 1
    else:
        return 0