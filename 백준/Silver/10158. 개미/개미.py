# 오른쪽 위 45도 방향으로 움직이기 시작한다는 말은
# 시작할 때 x, y가 증가한다는 것을 의미.  
# 대각선으로 생각하지 말고, x축에서 왔다갔다, y축에서 왔다갔다로 생각해라
# 경계면에 부딪히면 반사된다. > 가로길이의 양 끝에 도달하면 다시 되돌아간다는 뜻

# 격자 공간의 가로길이 w, 세로 길이 h
w, h = map(int, input().split())
# 초기 위치의 좌표값 p와 q
p, q = map(int, input().split())
# 개미가 움직일 시간 t
t = int(input())

# 이동하는 가로 좌표들, 세로 좌표들을 담을 리스트 생성
wPoints, hPoints = [], []
# 가로 좌표 수집
for i in range(w):
    wPoints.append(i)
for i in range(w, 0, -1):
    wPoints.append(i)
# 세로 좌표 수집 
for i in range(h):
    hPoints.append(i)
for i in range(h, 0, -1):
    hPoints.append(i) 
# p부터 t만큼 이동한 지점을 wPoint의 좌표에서 찾는다. (세로의 경우도 동일)
print(wPoints[(p+t)%(2*w)], hPoints[(q+t)%(2*h)])