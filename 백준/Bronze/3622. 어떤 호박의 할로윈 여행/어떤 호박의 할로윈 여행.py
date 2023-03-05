A, a, B, b, P = map(int, input().split())
# A나 B가 P보다 길 때 -> 못 만듬
if A>P or B>P:
    print('No')
# A와 B의 길이의 합이 P보다 작거나 같을 경우 가능
elif A+B<=P:
    print('Yes')
# B 안에 A가 쏙 들어갈 수 있으면 가능
elif b>=A:
    print('Yes')
# A 안에 B가 쏙 들어갈 수 있으면 가능
elif a>=B:
    print('Yes')
# 다 아니면 그냥 불가능임
else:
    print('No')