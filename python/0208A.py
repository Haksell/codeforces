import re

s = input()
print(re.sub(r"(WUB)+", " ", s).strip())
