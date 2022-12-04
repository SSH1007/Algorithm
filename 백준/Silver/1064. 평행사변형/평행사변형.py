# 점과 점 사이 거리 구하는 함수
def dist(a,b,c,d):
    return ((a-c)**2+(b-d)**2)**0.5

def judge():
    # 세 점의 좌표 입력
    ax,ay,bx,by,cx,cy=map(int, input().split())

    # 기울기 비교해서 세 점이 일직선인지 판별
    if (ax-bx)*(ay-cy) == (ax-cx)*(ay-by):
        print(-1.0)
        return

    # (최대 거리-최소 거리)*2 출력    
    A = dist(ax,ay,bx,by)
    B = dist(ax,ay,cx,cy)
    C = dist(bx,by,cx,cy)
    lst = [A+B,A+C, B+C]
    print(2*(max(lst)-min(lst)))
    return

judge()