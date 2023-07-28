def solution(score):
    answer = []
    lst = []
    for s in range(len(score)):
        lst.append((score[s][0]+score[s][1])/2)
    
    slst = sorted(list(set(lst)), reverse=True)
    visited = [0]*len(lst)
    cnt = 1
    for s in slst:
        flag = False
        for l in range(len(lst)):
            if lst[l] == s and not visited[l]:
                visited[l] = cnt
                flag = True
        if flag:
            cnt += visited.count(cnt)
        
    answer= visited
                
                
    return answer