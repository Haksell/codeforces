import re

for _ in range(int(input())):
    print("NO" if re.search(r"11.*00", input()) else "YES")
