N = int(input())
a = ~N + 1
print(32-bin(~(a^N)).count('1'))