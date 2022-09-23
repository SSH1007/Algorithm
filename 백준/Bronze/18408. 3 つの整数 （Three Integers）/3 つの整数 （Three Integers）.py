abc = list(map(int, input().split()))
one = abc.count(1)
two = abc.count(2)
print(1 if one>two else 2) 