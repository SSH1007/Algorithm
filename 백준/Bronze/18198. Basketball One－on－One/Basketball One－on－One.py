result = input()
aScore, bScore = 0, 0
for i in range(1,len(result),2):
    if result[i-1] == 'A':
        aScore+=int(result[i])
    elif result[i-1] == 'B':
        bScore+=int(result[i])
    
print('A' if aScore>bScore else 'B')