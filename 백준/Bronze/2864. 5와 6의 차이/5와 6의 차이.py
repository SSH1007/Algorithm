A, B = input().split()
maxDap, minDap = 0, 0

Amax = A.replace('5','6')
Amin = A.replace('6','5')
Bmax = B.replace('5','6')
Bmin = B.replace('6','5')
print(int(Amin)+int(Bmin),int(Amax)+int(Bmax))