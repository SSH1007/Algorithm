alpha = ''
while 1:
    ad = 1
    alpha = input()
    if alpha == '0':
        break
    for a in alpha:
        if a == '1':
            ad+=2
        elif a == '0':
            ad+=4
        else:
            ad+=3
        ad+=1
    print(ad)