import sys
input = lambda: sys.stdin.readline().rstrip()

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
# 방문 기록용 dic
memo = dict()
dap = 0


def DFS(r, c, bitmask, cnt):
    global dap
    idx = r*C+c
    # 이미 방문한 정보를 갖고 다시 방문했다면 리턴
    if (idx, bitmask) in memo:
        return memo[(idx, bitmask)]

    dap = max(dap, cnt)

    # 알파벳 개수는 26(최대수치)
    if dap == 26:
        return dap

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            next = maps[nr][nc]
            next_bit = 1 << (ord(next)-ord('A'))
            # 다음 방문할 알파벳 정보와 현재 방문 알파벳 정보가 다르다면
            if bitmask & next_bit == 0:
                # 알파벳 정보를 갱신하여 DFS
                # 동일한 좌표, 동일한 알파벳 목록이라도
                # 다른 경로를 통해 더 긴 경로를 찾을 수 있으므로 max 사용
                memo[(idx, bitmask)] = max(memo.get((idx, bitmask), 0), DFS(nr, nc, bitmask|next_bit, cnt+1))
    # 딕셔너리 값이 없어서 에러 뜨는걸 막기 위해 get으로 기본값 설정
    return memo.get((idx, bitmask), cnt)


start = maps[0][0]
start_bit = 1 << (ord(start)-ord('A'))
DFS(0, 0, start_bit, 1)
print(dap)