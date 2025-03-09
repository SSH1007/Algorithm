import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    ML, MR, TL, TR = input().split()
    # 민성이 올 바위, 태경이 보
    if ML==MR=='R' and (TL=='P'or TR=='P'):
        print("TK")
    # 민성이 올 보, 태경이 가위
    elif ML==MR=='P' and (TL=='S'or TR=='S'):
        print("TK")
    # 민성이 올 가위, 태경이 바위
    elif ML==MR=='S' and (TL=='R'or TR=='R'):
        print("TK")
    # 민성이 바위, 태경이 올 가위
    elif (ML=='R' or MR=='R') and TL==TR=='S':
        print("MS")
    # 민성이 가위, 태경이 올 보
    elif (ML=='S' or MR=='S') and TL==TR=='P':
        print("MS")
    # 민성이 보, 태경이 올 바위
    elif (ML=='P' or MR=='P') and TL==TR=='R':
        print("MS")
    else:
        print("?")


if __name__ == '__main__':
    main()