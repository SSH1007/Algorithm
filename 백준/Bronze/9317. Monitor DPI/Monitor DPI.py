while 1:
    D, RH, RV = map(float, input().split())
    if D == RH and RH == RV and D == 0:
        break
    W = (16*D)/(337**0.5)
    H = 9/16*W
    print('Horizontal DPI: %.2f' % round(RH/W, 2))
    print('Vertical DPI: %.2f' % round(RV/H, 2))