def dap():
    T = int(input())
    maxX, maxY, minX, minY = -10001, -10001, 10001, 10001
    for _ in range(T):
        x, y = map(int, input().split())
        if x>maxX:
            maxX = x
        if x<minX:
            minX = x
        if y>maxY:
            maxY = y
        if y<minY:
            minY = y
    print((maxX-minX)*(maxY-minY))
    
if __name__ == '__main__':
    dap()