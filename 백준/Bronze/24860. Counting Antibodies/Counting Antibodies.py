import sys
input = sys.stdin.readline
Vk, Jk = map(int, input().rstrip().split())
Vy, Jy = map(int, input().rstrip().split())
Vh, Dh, Jh = map(int, input().rstrip().split())

print(Vk*Jk*Vh*Dh*Jh + Vy*Jy*Vh*Dh*Jh)