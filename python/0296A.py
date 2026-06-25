# ruff: noqa: E731, E741
from collections import Counter

print(
    "YES"
    if int(input()) >= 2 * Counter(input().split()).most_common(1)[0][1] - 1
    else "NO"
)
