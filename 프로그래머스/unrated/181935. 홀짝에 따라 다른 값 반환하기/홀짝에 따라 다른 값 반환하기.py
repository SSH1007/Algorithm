def solution(n):
    answer = 0
    if n%2:
        lst = [i for i in range(1, n+1) if i%2]
        answer = sum(lst)
    else:
        lst = [i**2 for i in range(n+1) if i%2==0]
        print(lst)
        answer = sum(lst)
    return answer