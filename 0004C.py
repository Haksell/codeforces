from collections import defaultdict
import sys

input()
d = defaultdict(int)
for line in sys.stdin:
    line = line.strip()
    if d[line] == 0:
        print("OK")
    else:
        print(f"{line}{d[line]}")
    d[line] += 1
