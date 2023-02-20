# c=빨간색, z=노란색, n=파란색 잉크의 양
c, z, n = map(int, input().split())
# 노랑
y = int(input())
# 초록
g = int(input())
# 파랑
b = int(input())
# 보라
v = int(input())
# 빨강
r = int(input())
# 주황
o = int(input())
# 단색들부터 빼준다
c-=r
z-=y
n-=b

# 추가 빨강
cr = o/2+v/2
# 추가 노랑
zr = o/2+g/2
# 추가 파랑
nr = v/2+g/2

def func(c, cr):
    if c-cr>=0:
        print(0, end=' ')
    else:
        if abs(c-cr)>int(abs(c-cr)):
            print(round(abs(c-cr),1), end=' ')
        else:
            print(int(abs(c-cr)), end=' ')

func(c,cr)
func(z,zr)
func(n,nr)