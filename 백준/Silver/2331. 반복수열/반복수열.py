A, P = map(int, input().split())
lst = [A]
idx = 0
while 1:
    tmp = 0
    for a in str(A):
        tmp += int(a)**P
    A = tmp
    if tmp in lst:
        idx = lst.index(A)
        break
    lst.append(tmp)
print(idx)