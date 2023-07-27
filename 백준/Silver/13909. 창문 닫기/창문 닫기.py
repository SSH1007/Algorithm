N = int(input())
lst = []
for i in range(1, 45826):
    if i**2 <= N:
        lst.append(i)
print(len(lst))