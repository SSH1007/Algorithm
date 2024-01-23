N = int(input())
a = 4294967295 - N + 1
print(bin(a^N).count('1'))