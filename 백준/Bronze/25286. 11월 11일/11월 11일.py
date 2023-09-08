dic1 = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
dic2 = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
T = int(input())
for _ in range(T):
    y, m = map(int, input().split())
    leap = False
    if (y%4==0 and y%100) or y%400==0:
        leap = True
    if m > 1:
        print(y, m-1, dic2[m-1] if leap else dic1[m-1])
    else:
        print(y-1, 12, 31)