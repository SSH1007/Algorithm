m, seed, x1, x2 = map(int, input().split())


def ran():
    for a in range(0, 100):
        for c in range(0, 100):
            if (a*seed+c)%m == x1 and (a*x1+c)%m == x2:
                print(a, c)
                return


ran()