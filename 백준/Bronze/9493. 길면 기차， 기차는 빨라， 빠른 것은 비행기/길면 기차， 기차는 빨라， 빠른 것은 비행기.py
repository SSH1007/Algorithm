while 1:
    M, A, B = map(int, input().split())
    if M == 0:
        break
    tmp = round(M/A*3600 - M/B*3600)
    hour = int(tmp // 3600)
    minute = int((tmp % 3600) // 60)
    second = int(tmp % 60)
    print('%d:%02d:%02d' % (hour, minute, second))