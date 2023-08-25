T = int(input())
for _ in range(T):
    input()
    milk, yolk, sugar, salt, wheat = map(int, input().split())
    banana, berry, chocolate, walnut = map(int, input().split())
    milk /= 8
    yolk /= 8
    sugar /= 4
    wheat /= 9
    dough = int(16 * min(milk, yolk, sugar, salt, wheat))
    berry //= 30
    chocolate //= 25
    walnut //= 10
    fruit = sum((banana, berry, chocolate, walnut))
    print(min(dough, fruit))