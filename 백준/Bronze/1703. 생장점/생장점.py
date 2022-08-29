while 1:
    dap = 1 
    seedling = [1,0]
    lst= list(map(int, input().split()))
    if lst == [0]:
        break
    age = lst[0]
    lst = seedling + lst[1:]
    for i in range(age+1):
        dap *= lst[2*i]
        dap -= lst[2*i+1]
    print(dap)