import sys
input = sys.stdin.readline
word = list(input().rstrip())
rest = []
M = int(input().rstrip())
for _ in range(M):
    command = list(input().rstrip().split())
    if command[0] == 'L' and word:
        rest.append(word.pop())
    elif command[0] == 'D' and rest:
        word.append(rest.pop())
    elif command[0] == 'B' and word:
        word.pop()
    elif command[0] == 'P':
        word.append(command[1])
print(''.join(word+rest[::-1]))