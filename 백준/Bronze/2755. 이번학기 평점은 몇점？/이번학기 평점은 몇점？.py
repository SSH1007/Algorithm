def customRound(n):
    n *= 100
    return (int(n)+1)/100 if n-int(n)>=0.5 else int(n)/100


dic = {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}
N = int(input())
dap, mom = 0, 0
for _ in range(N):
    subject, credit, score = input().split()
    dap += (dic[score]*int(credit))
    mom += int(credit)
print('{0:.2f}'.format(customRound(dap/mom)))