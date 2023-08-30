def solution(id_list, report, k):
    answer = []
    report = list(set(report))
    # count = 누가 얼마나 신고당했는지 기록
    count = dict()
    # who = 누가 누구를 신고했는지 기록
    who = dict()
    for r in report:
        w, b = r.split()
        if not b in count:
            count[b] = 1
        else:
            count[b] += 1
            
        if not w in who:
            who[w] = [b]
        else:
            if not b in who[w]:
                who[w].append(b)
            
    # k회 이상 신고당해 정지당한 유저들
    banned = list(filter(lambda x: x[1]>=k, list(count.items())))

    for id in id_list:
        tmp = 0
        if id in who:
            for b in banned:
                if b[0] in who[id]:
                    tmp += 1
            answer.append(tmp)
        else:
            answer.append(0)
    return answer