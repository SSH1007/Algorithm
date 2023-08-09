while 1:
    a = input()
    if a == 'EOI':
        break
    if 'nemo' in a.lower():
        print('Found')
    else:
        print('Missing')