import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    # 이등변삼각형 ABC의 수선 AD 설정
    # 직각삼각형 ADC는 피타고라스의 정리 사용 가능
    # AD^2 = AC^2 - DC^2
    # 여기서 DC는 BC의 절반에 해당하는 값이므로 이렇게 변형할 수 있다.
    # AD^2 = AC^2 - (BC/2)^2

    # BC를 지나는 점 i에 대해서 Ai는 피타고라스 정리에 의해
    # Ai^2 = iD^2 + AD^2
    # iD는 BC의 절반에서 Bi만큼을 빼준 값이므로
    # Ai^2 = (BC/2 - Bi)^2 + AD^2

    # 위에서 구한 AD^2와 더해주면
    # Ai^2 = -BC*Bi + Bi^2 + AC^2

    # 나머지 Bi*Ci는 Bi = BC-Bi이므로
    # (BC-Bi)*Bi = BC*Bi-Bi^2

    # 위의 Ai^2와 더해주면?
    # AC^2만 남는다.
    # AC는 N이므로 f(i)는 N^2
    # 따라서 답은
    print((N**2)*K)
    

if __name__ == '__main__':
    main()