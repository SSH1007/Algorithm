while 1:
    S = input()
    accept = False
    if S == 'end':
        break
    ja = 'bcdfghjklmnpqrstvwxyz'
    mo = 'aeiou'
    jaCnt, moCnt = 0, 0

    # 1. 모음 하나를 반드시 포함
    if 'a' in S or 'e' in S or 'i' in S or 'o' in S or 'u' in S:
        accept = True

    if accept:
        former = ''
        # 2. 모음 혹은 자음이 연속 3개 붙어있으면 안된다
        for n in range(len(S)):
            if S[n] in ja:
                jaCnt += 1
                moCnt = 0
            elif S[n] in mo:
                moCnt += 1
                jaCnt = 0
            if moCnt == 3 or jaCnt == 3:
                accept = False
                break

            # 3. ee나 oo를 제외하고, 같은 글자가 연속으로 두번 오면 안된다
            if former != S[n]:
                former = S[n]
            else:
                if S[n] != 'e' and S[n] != 'o':
                    accept = False
                    break

    # 결과값 출력
    if accept:
        print(f'<{S}> is acceptable.')
    else:
        print(f'<{S}> is not acceptable.')