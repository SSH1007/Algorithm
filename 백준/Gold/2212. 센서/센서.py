import sys
input = sys.stdin.readline


def f():
    # 센서의 수 N, 센서의 좌표는 겹칠수도 있음 (모두 겹칠 가능성 有)
    N = int(input().rstrip())
    # 집중국의 최대 설치 가능 개수 K. 수신 가능영역의 길이는 0 이상
    K = int(input().rstrip())
    sensors = sorted(list(set(map(int, input().rstrip().split()))))
    if N <= K:
        # 집중국이 센서 수보다 많거나 같으면 센서마다 집중국을 놓으면 되니
        # 수신 가능 영역의 길이는 0이 된다.
        return 0
    cha = []
    for i in range(1, len(sensors)):
        cha.append(sensors[i]-sensors[i-1])
    cha.sort()
    for _ in range(K-1):
        cha.pop()
    return sum(cha)


print(f())