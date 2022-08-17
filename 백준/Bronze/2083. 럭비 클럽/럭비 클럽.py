while 1:
    lst = input().split()
    if lst[0] == '#':
        break
    if int(lst[1]) > 17 or int(lst[2])>=80:
        print(lst[0],'Senior')
    else:
        print(lst[0],'Junior')