import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    clst = [0]*3
    mlst = [0]*3
    for i in range(3):
        b, m = map(int, input().split())
        clst[i] = b
        mlst[i] = m

    for i in range(100):
        j = i%3 # 현재 순번
        milk = mlst[j] # 현재 양동이 안의 우유 양
        k = (j+1)%3  # 다음 순번
        # 양동이 넘치지 않을 정도로 옮길 우유 양 조정
        if clst[k] < milk + mlst[k]:
            milk = clst[k] - mlst[k]
        mlst[k] += milk
        mlst[j] -= milk

    print(*mlst, sep='\n')


if __name__ == '__main__':
    main()