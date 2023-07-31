def solution(S):
    answer = True
    st = ''
    for s in S:
        st+=s.lower()
    p = st.count('p')
    y = st.count('y')
    
    if p == 0 and y == 0:
        pass
    else:
        if p!=y:
            answer = False

    return answer