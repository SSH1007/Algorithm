import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    pic = [list(input().split()) for _ in range(15)]
    for i in range(15):
        for j in range(15):
            x = pic[i][j]
            if x == 'w':
                print('chunbae')
                return
            elif x == 'b':
                print('nabi')
                return
            elif x == 'g':
                print('yeongcheol')
                return


if __name__ == '__main__':
    main()