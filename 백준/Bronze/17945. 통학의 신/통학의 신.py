A, B = map(int, input().split())
x1 = (-2*A + int(((4*(A**2) - 4*B))**0.5))//2
x2 = (-2*A - int(((4*(A**2) - 4*B))**0.5))//2
lst = sorted(list(set([x1, x2])))
print(*lst)