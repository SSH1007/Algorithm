T = int(input())
for _ in range(T):
    A, B, C, D, E = map(int, input().split())
    price = (A*350.34) + (B*230.90) + (C*190.55) + (D*125.30) + (E*180.90)
    print(f'${price:.2f}')