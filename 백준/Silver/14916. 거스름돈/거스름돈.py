n = int(input())
# 1 -1
# 2 1
# 3 -1
# 4 2
# 5 1
# 6 3
# 7 2
# 8 4

# 9 3
# 10 2
# 11 4
# 12 3
# 13 5
# 14 4
# 15 3
# 16 5
# 17 4
# 18 6
# 19 5
lst1 = [0,-1,1,-1,2,1,3,2,4]
lst2 = [0 for _ in range(100000)]
lst = lst1+lst2
if n <= 8:
    print(lst[n])
else:
    for i in range(9, n+1):
        lst[i] = lst[i-5]+1
    print(lst[n])