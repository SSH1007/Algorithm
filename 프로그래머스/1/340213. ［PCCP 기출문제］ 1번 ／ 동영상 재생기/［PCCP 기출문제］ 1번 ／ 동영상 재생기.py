def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    v = list(map(int, video_len.split(':')))
    vl = v[0]*60+v[1]
    p = list(map(int, pos.split(':')))
    ps = p[0]*60+p[1]
    ops = list(map(int, op_start.split(':')))
    os = ops[0]*60+ops[1]
    ope = list(map(int, op_end.split(':')))
    oe = ope[0]*60+ope[1]
    if os <= ps <= oe:
        ps = oe
    for c in commands:
        if c == 'prev':
            ps = max(ps-10, 0)
        else:
            ps = min(ps+10, vl)
        if os <= ps <= oe:
            ps = oe
    # print(ps, ps//60, ps%60)
    answer = f'{str(ps//60).zfill(2)}:{str(ps%60).zfill(2)}'
    return answer