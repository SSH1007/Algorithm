def draw_star(N):
    if N == 1:
        return ["*"]
    Stars = draw_star(N//3)
    tmp = []
    for s in Stars:
        tmp.append(s*3)
    for s in Stars:
        tmp.append(s+' '*len(s)+s)
    for s in Stars:
        tmp.append(s*3)
    return tmp


N = int(input())
lst = draw_star(N)
print('\n'.join(lst))