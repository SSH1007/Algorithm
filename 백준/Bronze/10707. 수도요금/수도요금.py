# X사의 1리터당 요금
A = int(input())
# Y사의 기본요금 
B = int(input())
# Y사의 요금이 기본요금이 되는 사용량의 상한
C = int(input())
# Y사의 1리터당 추가요금
D = int(input())
# JOI군의 집에서 사용하는 한달간 수도의 양
E = int(input())

Xmoney = E*A
if E<=C:
    Ymoney = B
else:
    Ymoney = B+(E-C)*D
print(min(Xmoney,Ymoney))