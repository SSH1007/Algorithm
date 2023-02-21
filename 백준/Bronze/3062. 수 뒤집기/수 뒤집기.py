T = int(input())
for _ in range(T):
    N = int(input())
    # N을 뒤집은 수
    revN = int(str(N)[::-1])
    # 원래 수와 뒤집은 수의 합
    hap = N+revN
    # 합을 뒤집은 수
    revhap = int(str(hap)[::-1])
    if hap == revhap:
        print('YES')
    else:
        print('NO')