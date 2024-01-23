v = 0b10000
watch = [[' ']*7 for _ in range(4)]
time = input()
for t in range(4):
    bt = bin(v|int(time[t]))[3:]
    for i in range(4):
        watch[i][2*t] = '.' if bt[i] == '0' else '*'
for w in watch:
    w[3] = '   '
    print(''.join(w))