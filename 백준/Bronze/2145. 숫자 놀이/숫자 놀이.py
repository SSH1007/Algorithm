while 1:
    N = input()
    if int(N)==0:
        break
    
    while 1:
        std = 0
        for n in range(len(N)):
            std+=int(N[n])
        if len(str(std))==1:
            break
        else:
            N = str(std)
    print(std)