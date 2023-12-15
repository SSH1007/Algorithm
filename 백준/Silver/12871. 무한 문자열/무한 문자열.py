s = input()
t = input()

def GCD(a, b):
    while b > 0:
        a, b = b, a%b
    return a

l = len(s)*len(t)//GCD(len(s), len(t))
ss, tt = '', ''
for _ in range(l//len(s)):
    ss += s
for _ in range(l//len(t)):
    tt += t
print(1 if tt==ss else 0)