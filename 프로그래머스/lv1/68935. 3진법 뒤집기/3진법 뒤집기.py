def solution(n):
    answer = 0
    tri = ''
    while n > 0:
        a = n%3
        n//=3
        tri = str(a)+tri
    tri = tri[::-1]
    
    for t in range(len(tri)):
        answer += int(tri[len(tri)-t-1])*(3**t)
        
    return answer