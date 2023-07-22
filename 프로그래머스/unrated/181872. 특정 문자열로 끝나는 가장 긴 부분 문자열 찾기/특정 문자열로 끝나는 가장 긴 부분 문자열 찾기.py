def solution(myString, pat):
    answer = ''
    mys = myString[::-1]
    tap = pat[::-1]
    idx = mys.find(tap)
    dap = mys[idx:]
    answer = dap[::-1]
    return answer