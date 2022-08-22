for _ in range(3):
    Ahs, Ams, Ass, Ahe, Ame, Ase = map(int,input().split())
    AworkTime = Ahe*3600+Ame*60+Ase -(Ahs*3600+Ams*60+Ass)
    print(AworkTime//3600, (AworkTime%3600)//60, (AworkTime%3600)%60)