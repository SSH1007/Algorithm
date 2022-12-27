# 최대공약수를 구하는 유클리드 호제법
def getGCD(a,b):
    while b:
        a, b = b, a % b
    return a

# 테스트 케이스 T 받고
T = int(input())
# T만큼 반복
for _ in range(T):
    # 두 정수 a, b 받고
    a, b = map(int, input().split())
    # 최대공약수 구하고
    gcd = getGCD(a,b)
    # 최소공배수 구하고 
    lcm = a*b//(gcd)
    # 출력한다
    print(lcm, gcd)