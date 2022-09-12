for _ in range(int(input())):
    dic = {'TTT': 0, 'TTH': 0, 'THT': 0, 'THH': 0, 'HTT': 0, 'HTH': 0, 'HHT': 0, 'HHH': 0}
    toss = input()
    for i in range(38):
        dic[toss[i:i+3]] += 1
    for n in dic.values():
        print(n, end=' ')
    print()