while 1:
    try:
        H, P = map(int, input().split())
        print(f'{H/P:.2f}')
    except:
        break