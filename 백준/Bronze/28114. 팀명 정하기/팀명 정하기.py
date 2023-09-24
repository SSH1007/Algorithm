P1, Y1, S1 = input().split()
P2, Y2, S2 = input().split()
P3, Y3, S3 = input().split()
a = [int(Y1) % 100, int(Y2) % 100, int(Y3) % 100]
a.sort(key= lambda x: x)
lst = [(S1[0], int(P1)), (S2[0], int(P2)), (S3[0], int(P3))]
lst.sort(key=lambda x: -x[1])
b = ''.join([l[0] for l in lst])
print(''.join(map(str,a)))
print(b)