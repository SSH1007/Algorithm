def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    idx, idx1, idx2 = 0, 0, 0
    while idx < len(goal):
        if idx2 >= len(cards2) and cards1[idx1] != goal[idx]:
            answer = 'No'
            break
        if idx1 >= len(cards1) and cards2[idx2] != goal[idx]:
            answer = 'No'
            break
        if idx1 < len(cards1) and cards1[idx1] == goal[idx]:
            idx1 += 1
            idx += 1
        if idx2 < len(cards2) and cards2[idx2] == goal[idx]:
            idx2 += 1
            idx += 1
        
    return answer