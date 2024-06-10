def main():

    def isPrime(n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                # ex) 12 % 2 == 0이면 12의 소인수는 12//2인 6의 소인수의 개수 + 1
                cnt[n] = cnt[n//i] + 1
                # 1과 자기 자신이 아닌 다른 수로 나눠지므로 소수 아님
                return 0
        # 소수는 소인수분해 후 약수의 개수 1
        cnt[n] = 1
        # 소수 맞음
        return 1


    A, B = map(int, input().split())
    # 소인수분해 시 소수 개수를 담는 리스트
    cnt = [0]*(B+1)
    # 소수 판정 리스트
    prime = [0]*(B+1)

    for i in range(2, B+1):
        prime[i] = isPrime(i)
    dap = 0
    for i in range(A, B+1):
        dap += prime[cnt[i]]
    print(dap)


if __name__ == '__main__':
    main()