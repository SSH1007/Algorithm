T = int(input())
for t in range(T):
    Good = list(map(int, input().split()))
    Evil = list(map(int, input().split()))
    Goodpt = Good[0]+Good[1]*2+Good[2]*3+Good[3]*3+Good[4]*4+Good[5]*10
    Evilpt = Evil[0]+Evil[1]*2+Evil[2]*2+Evil[3]*2+Evil[4]*3+Evil[5]*5+Evil[6]*10
    if Goodpt > Evilpt:
        print(f'Battle {t+1}: Good triumphs over Evil')
    elif Goodpt < Evilpt:
        print(f'Battle {t+1}: Evil eradicates all trace of Good')
    else:
        print(f'Battle {t+1}: No victor on this battle field')