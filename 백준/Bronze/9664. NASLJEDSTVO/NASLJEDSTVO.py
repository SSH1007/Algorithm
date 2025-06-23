def F(N, O):
    min_x = None
    max_x = None
    for q in range(1, O + 1):
        x = O + q
        if x // N == q:
            if min_x is None or x < min_x:
                min_x = x
            if max_x is None or x > max_x:
                max_x = x
    return min_x, max_x


N = int(input())
O = int(input())
min_x, max_x = F(N, O)
print(min_x, max_x)