while 1:
    ew = float(input())
    if '-' in str(ew):
        break
    mw = ew*0.167
    print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (ew,mw))