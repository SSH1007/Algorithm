def solution(message, spoiler_ranges):
    answer = 0
    # 문자별 s,e,w 목록 만들기
    start = 0 if message[0] != ' ' else 1
    words = []
    for m in message.split():
        words.append([start, start+len(m), m])
        start += len(m)+1
    # 스포 방지 구간 체크
    covered = [False]*len(message)
    for s, e in spoiler_ranges:
        for i in range(s, e+1):
            covered[i] = True
    # 중요하지 않은 단어 목록 만들기
    common = set()
    for s, e, w in words:
        isCovered = False
        for i in range(s, e):
            if covered[i]:
                isCovered = True
                break
        if not isCovered:
            common.add(w)
    # 스포 방지 단어 하나씩 까면서 체크
    # (단어의 모든 문자 공개 && 중복 NO)
    opened = [False]*len(message)
    used = set()
    for ss, se in spoiler_ranges:
        for i in range(ss, se+1):
            opened[i] = True
        for s, e, w in words:
            isSpoiler = False
            for i in range(s, e):
                if covered[i]:
                    isSpoiler = True
                    break
            if not isSpoiler:
                continue
            allOpened = True
            for i in range(s, e):
                if covered[i] and not opened[i]:
                    allOpened = False
                    break
            if not allOpened:
                continue
            if w not in common and w not in used:
                used.add(w)
                answer += 1
    return answer