kan = ['6','7','8','9','0','1','2','3','4','5']
ji = ['I','J','K','L','A','B','C','D','E','F','G','H']
N = int(input())
dap = ji[N%12] + kan[N%10]
print(dap)