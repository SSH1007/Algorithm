def solution(a, b, c):
    answer = 0
    s = set((a,b,c))
    if len(s)==3:
        answer = a+b+c
    elif len(s)==2:
        answer = (a+b+c)*(a**2+b**2+c**2)
    elif len(s)==1:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    return answer