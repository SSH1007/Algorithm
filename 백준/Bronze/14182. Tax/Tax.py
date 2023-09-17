while 1:
    N = int(input())
    if N:
        if 5000000 >= N > 1000000:
            print(int(N*0.9))
        elif N > 5000000:
            print(int(N*0.8))
        else:
            print(N)
        continue
    break