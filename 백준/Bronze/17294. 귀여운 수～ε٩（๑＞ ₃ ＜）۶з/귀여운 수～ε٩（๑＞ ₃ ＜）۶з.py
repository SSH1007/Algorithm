N = input()


def F():
    lst = []
    for i in range(1, len(N)):
        lst.append(int(N[i]) - int(N[i-1]))
    for i in range(1, len(lst)):
        if lst[i] != lst[i-1]:
            return 0
    return 1


if F():
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
else:
    print('흥칫뿡!! <(￣ ﹌ ￣)>')