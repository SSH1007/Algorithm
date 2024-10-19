import sys
input = lambda: sys.stdin.readline().rstrip()
from math import ceil


def main():
    dap = float('inf')
    N, H_Atk = map(int, input().split())
    dungeon = [list(map(int, input().split())) for _ in range(N)]
    # N번째(마지막) 방에 있는 용을 쓰러뜨리기 위한 최소의 H_maxHP 구하기
    # 최악의 경우, 123456개의 방에 몬스터만 있고, 모두 공격력/체력이 백만일 수 있다.
    # 게다가 용사의 공격력은 1
    s, e = 1, 123456*(1000000**2)+1
    while s <= e:
        mid = (s+e)//2
        curHP, curATK = mid, H_Atk
        status = 1  # 1: 생존, 0: 사망
        for n in range(N):
            # t: 1이면 공격력이 a, 생명력 h인 몬스터가 방에 있다
            # t: 2면 용사 공격력 += a, 생명력 += h 회복
            t, a, h = dungeon[n]
            if t == 1:
                # 용사가 몬스터에게 맞으면 죽는 횟수
                H_endure = ceil(curHP / a)
                # 몬스터가 용사에게 맞으면 죽는 횟수
                # = 몬스터는 후공이므로 몬스터가 죽을때까지
                #   서로 공격을 주고받는 횟수이기도 하다
                M_endure = ceil(h / curATK)
                # 용사가 선공이므로 유리
                if H_endure >= M_endure:
                    # 이겼을 경우 마지막은 용사만 때리므로 -1
                    curHP -= (M_endure-1)*a
                else:
                    status = 0
                    break
            else:
                curATK += a
                curHP += h
                # 최대 체력을 초과했을 경우, 정상화
                curHP = min(curHP, mid)

        if status:  # 현재 조건으로 던전 공략에 성공했다면
            dap = mid
            e = mid-1
        else:
            s = mid+1
    print(dap)


if __name__ == '__main__':
    main()