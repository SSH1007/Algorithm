import sys
while 1:
    try:
        txt = list(sys.stdin.readline().strip())
        if txt == []:
            break
        for t in range(len(txt)):
            if txt[t] == 'i':
                txt[t] = 'e'
            elif txt[t] == 'e':
                txt[t] = 'i'
            elif txt[t] == 'I':
                txt[t] = 'E'
            elif txt[t] == 'E':
                txt[t] = 'I'
        print(('').join(txt))
    except:
        break