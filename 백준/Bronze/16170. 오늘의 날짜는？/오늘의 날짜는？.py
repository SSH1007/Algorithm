from datetime import datetime

b = datetime.today().year
c = datetime.today().month
d = datetime.today().day
print(b)
print('0'+str(c) if c<10 else c)
print(d)