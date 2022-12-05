# 한번씩만 방문하는가?
# 마지막 도착지에서 시작점으로 돌아갈 수 있는가?
# 36칸의 체스판 리스트 생성(도착 확인용)
visited = [[0]*6 for _ in range(6)]
duplicate = False   # 중복 방문 여부
knight = False      # 나이트 행마법 위반 여부
lst = []            # 이동 지점 목록
# 36번 입력
for _ in range(36):
    path = input()
    # 알파벳은 아스키코드로 처리
    x = ord(path[0])-65
    y = int(path[1])-1
    # 만약 이미 방문했다면 중복 방문 여부를 True로
    if visited[x][y]:
        duplicate = True
    # 아니면 방문 표시
    else:
        visited[x][y] = 1
    # 이동 지점 목록을 추가한다
    lst.append((x,y))

# 이동 지점 목록 끝에 시작점을 다시 넣어준다
first = lst[0]
lst.append(first)

# 36번 순회
for i in range(36):
    # 만약 나이트 행마법을 위반했다면 위반 여부를 True로 (이전 지점과 x가 2, y가 1 차이나거나, x가 1, y가 2 차이 나야 됨)
    if not (abs(lst[i+1][0]-lst[i][0])==2 and abs(lst[i+1][1]-lst[i][1])==1) and not (abs(lst[i+1][0]-lst[i][0])==1 and abs(lst[i+1][1]-lst[i][1])==2):
        knight = True

if duplicate or knight:
    print('Invalid')
else:
    print('Valid')