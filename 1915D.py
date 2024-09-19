import re

for _ in range(int(input())):
    input()
    s = input()
    syllables = re.findall(r"[bcd]?[ae][bcd]", s[::-1])
    print(".".join(syllables)[::-1])
