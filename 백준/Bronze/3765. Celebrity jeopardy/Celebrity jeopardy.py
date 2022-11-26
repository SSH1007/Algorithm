lst = []
while True:
    try:
        a = input().strip()
        lst.append(a)
    except:
        break
for l in lst:
    print(l)