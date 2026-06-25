# ruff: noqa: E731, E741
import re

for _ in range(int(input())):
    input()
    print("YES" if re.fullmatch(r"m+e+o+w+", input(), re.IGNORECASE) else "NO")
