import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    crains = sorted(list(map(int, input().split())), reverse=True)
    _ = int(input())
    boxes = sorted(list(map(int, input().split())), reverse=True)

    # 가장 무거운 박스를 가장 중량 제한이 큰 크레인이 못 옮길 경우
    if crains[0] < boxes[0]:
        print(-1)
        exit(0)

    # 박스를 크레인마다 분배.
    # 가벼운 박스는 무게 제한이 큰 크레인에게 옮길 수 있음
    min = 0
    while boxes:
        # 힘이 센 크레인부터 하나씩
        for crain in crains:
            # 가장 무거운 상자부터
            for box in boxes:
                # 박스들은 있는데,
                # 가장 가벼운 무게조차 해당 크레인이 옮길 수 없는 무게라면 포기하고
                # 다른 크레인에게 맡긴다
                if boxes and crain < boxes[-1]:
                    break
                # 해당 크레인이 옮길 수 있으면
                if crain >= box:
                    # 박스 옮기기
                    boxes.remove(box)
                    break
        min += 1
    print(min)


if __name__ == '__main__':
    main()