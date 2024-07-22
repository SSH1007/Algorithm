import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    sound = input()
    idx = 0
    flag = True
    while flag and idx < len(sound):
        if sound[idx] == '0':
            if idx+1 < len(sound) and sound[idx+1] == '1':
                idx += 2
            else:
                flag = False
        else:  # 1로 시작하는 경우
            # 무조건 0이 2개는 붙어있어야 함
            zeroCnt = 0
            idx += 1
            while idx < len(sound) and sound[idx] == '0':
                zeroCnt += 1
                idx += 1

            if zeroCnt < 2 or idx == len(sound):
                flag = False
            else:
                idx += 1
                while 1:
                    if idx >= len(sound):
                        # 길이 제한 초과
                        break
                    if sound[idx] == '0':
                        # '01' 판정으로 go
                        break

                    if idx+2 < len(sound) and sound[idx:idx+3] == '100':
                        # 1으로 시작하는 패턴 재시작
                        break

                    idx += 1

    print('SUBMARINE' if flag else 'NOISE')


if __name__ == '__main__':
    main()