N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

minusOne, zero, one = 0,0,0
def cnt(x,y,n):
    global minusOne, zero, one
    tmp = papers[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if tmp!=papers[i][j]:
                for k in range(3):
                    for l in range(3):
                        cnt(x+k*n//3,y+l*n//3,n//3)
                return
    if tmp == -1:
        minusOne+=1
    elif tmp == 0:
        zero +=1
    else:
        one += 1

cnt(0,0,N)
print(minusOne)
print(zero)
print(one)