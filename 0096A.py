import re

print("YES" if re.search(r"0{7}|1{7}", input()) else "NO")
