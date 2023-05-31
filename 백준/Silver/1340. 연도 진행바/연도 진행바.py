import sys
input = sys.stdin.readline
month = {'January':1, 'February':2, 'March':3, 'April':4, 'May':5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November':11, 'December':12}
leapMonth = [0,[31,31],[28,29],[31,31],[30,30],[31,31],[30,30],[31,31],[31,31],[30,30],[31,31],[30,30],[31,31]]
m, d, y, hm = input().rstrip().split()


currentTime = 0
allTime = 0
if int(y)%400==0 or (int(y)%4==0 and int(y)%100):
    for i in range(1, month[m]):
        currentTime += leapMonth[i][1]
    currentTime = currentTime*24*60
    allTime = 366*24*60
else:
    for i in range(1, month[m]):
        currentTime += leapMonth[i][0]
    currentTime = currentTime*24*60
    allTime = 365*24*60

dm = (int(d[:-1])-1)*24*60
hh, mm = map(int, hm.split(':'))
print((currentTime+dm+hh*60+mm)/allTime*100)