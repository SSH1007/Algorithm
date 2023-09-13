N = int(input())
levelup, elixir = 0, 4
case = [8, 4, 2, 1]
if N > 229:
    levelup, elixir = 1, 4
elif N > 219:
    levelup, elixir = 230 - N if 230 - N < 2 else 2, 3
elif N > 209:
    levelup, elixir = 220 - N if 220 - N < 4 else 4, 2
else:
    levelup, elixir = 210 - N if 210 - N < 8 else 8, 1
if elixir != 4:
    if case[elixir] >= levelup:
        elixir += 1
print(elixir)