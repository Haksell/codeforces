# ruff: noqa: E731, E741
import re

s = input()
print(re.sub(r"(WUB)+", " ", s).strip())
