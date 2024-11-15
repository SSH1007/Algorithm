Px1, Py1, Px2, Py2 = map(int, input().split())
Qx1, Qy1, Qx2, Qy2 = map(int, input().split())

if (Qx2==Px1 and Qy1==Py2) or (Qx1==Px2 and Qy1==Py2) or \
        (Qx2==Px1 and Qy2==Py1) or (Qx1==Px2 and Qy2==Py1):
    print('POINT')
    exit(0)


if (Px2 < Qx1) or (Py2 < Qy1) or (Qy2 < Py1) or (Qx2 < Px1):
    print('NULL')
    exit(0)

if (Px2==Qx1) or (Py2==Qy1) or (Px1==Qx2) or (Py1==Qy2):
    print('LINE')
    exit(0)

print('FACE')