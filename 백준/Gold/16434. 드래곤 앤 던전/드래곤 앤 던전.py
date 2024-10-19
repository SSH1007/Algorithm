import sys
input = lambda: sys.stdin.readline().rstrip()
from math import ceil


def main():
    N, H_ATK = map(int, input().split())
    dungeon = [list(map(int, input().split())) for _ in range(N)]
    # 몬스터들한테 받은 대미지들을 모두 합한 뒤 거기에 1을 더하는 방식
    curHP, minHP = 0, 0
    for n in range(N):
        # t: 1이면 공격력이 a, 생명력 h인 몬스터가 방에 있다
        # t: 2면 용사 공격력 += a, 생명력 += h 회복
        t, a, h = dungeon[n]
        if t == 1:
            # 몬스터가 용사에게 맞으면 죽는 횟수
            # = 몬스터는 후공이므로 몬스터가 죽을때까지
            #   서로 공격을 주고받는 횟수이기도 하다
            M_endure = ceil(h / H_ATK)
            # 이겼을 경우 마지막은 용사만 때리므로 -1
            curHP -= (M_endure-1)*a
            minHP = min(minHP, curHP)
        else:
            H_ATK += a
            curHP += h
            # 최대 체력을 초과했을 경우, 정상화
            curHP = min(curHP, 0)
    print((minHP*-1)+1)


if __name__ == '__main__':
    main()