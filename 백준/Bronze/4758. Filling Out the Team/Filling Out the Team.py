while 1:
    a,b,c=input().split()
    a,b,c=float(a),int(b),int(c)
    if a==0 and b==0 and c==0: break
    tmp=[]
    if a<=4.5 and b>= 150 and c>=200: 
        tmp.append("Wide Receiver")
    if a<=6.0 and b>= 300 and c>=500: 
        tmp.append("Lineman") 
    if a<=5.0 and b>= 200 and c>=300: 
        tmp.append("Quarterback")
    if tmp:
        print(*tmp)
    else:
        print("No positions")