# 최장 증가 부분 수열 : 2565. 전기줄
import sys
input = sys.stdin.readline


def main():
    # 남아있는 모든 전깃줄이 서로 교차하지 않기 위해 없애야 하는 최소 개수 구하기
    # => 남아있는 모든 전깃줄이 서로 교차하지 않는 최대 개수 구헤서 전체에서 빼면 된다.
    N = int(input().rstrip())
    info = [list(map(int, input().rstrip().split())) for _ in range(N)]
    # A전봇대 기준으로 B전봇대 정렬
    info.sort(key=lambda x: x[0])
    # B 전봇대 0번째 위치로 dp 초기값 설정
    dp = [info[0][1]]
    for i in range(1, N):
        # info[i][1]가 dp 마지막 수와 비교했을 때 증가한다면 dp에 추가
        if dp[-1] < info[i][1]:
            dp.append(info[i][1])

        # 그렇지 않을 경우 info[i][1]가 dp 안에 위치할 지점을 찾아서 값 교체
        # (해당 과정을 통해, dp는 오름차순으로 정렬된 형태가 된다)
        else:
            s, e = 0, len(dp)-1
            while s <= e:
                mid = (s+e)//2
                if dp[mid] > info[i][1]:
                    e = mid-1
                else:
                    s = mid+1
            dp[s] = info[i][1]
    print(N-len(dp))


if __name__ == '__main__':
    main()