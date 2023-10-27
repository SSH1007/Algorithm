while 1:
    bit = input()
    if bit == '#':
        break
    if bit[-1] == 'o':
        # 홀수
        if bit.count('1')%2:
            bit = bit.replace('o', '0')
        else:
            bit = bit.replace('o', '1')
    elif bit[-1] == 'e':
        # 짝수
        if bit.count('1')%2:
            bit = bit.replace('e', '1')
        else:
            bit = bit.replace('e', '0')
    print(bit)