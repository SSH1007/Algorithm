N = input()
for n in range(len(N)):
    print(chr(((ord(N[n])%65)-3)%26+65), end = '')