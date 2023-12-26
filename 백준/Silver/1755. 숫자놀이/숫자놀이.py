dic = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine', '0':'zero'}
M, N = map(int, input().split())
lst = []
for i in range(M, N+1):
    tmp = str(i)
    eng = ''
    for t in range(len(tmp)):
        if t != 0:
            eng += ' '
        eng += dic[tmp[t]]
    lst.append((i, eng))
lst.sort(key= lambda x: x[1])
for i in range(len(lst)):
    print(lst[i][0], end=' ')
    if i % 10 == 9:
        print()