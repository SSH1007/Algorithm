n = int(input())
if n%8 == 1:
    print(1)
if n%8 == 2 or n%8 == 0:
    print(2)
if n%8 == 3 or n%8 == 7:
    print(3)
if n%8 == 4 or n%8 == 6:
    print(4)
if n%8 == 5:
    print(5)