s = input() + "#"
res = sorted(range(len(s)), key=s.__getitem__)
vals = [0] * len(s)
for i in range(1, len(s)):
    vals[i] = vals[i - 1] + (s[res[i]] != s[res[i - 1]])
size = 1
while size < len(s):
    size <<= 1
