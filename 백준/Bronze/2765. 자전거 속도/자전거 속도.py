t = 1
d, m = 0, 0
pi = 3.1415927
while 1:
    j, h, s = map(float, input().split())
    if h == 0:
        break
    d = j/(12*5280)*pi*h
    m = d/s*3600
    print('Trip #{}: {:.2f} {:.2f}'.format(t, round(d,2), round(m,2)))
    t += 1