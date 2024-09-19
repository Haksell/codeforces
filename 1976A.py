import re


def is_sorted(a):
    return all(y >= x for x, y in zip(a, a[1:]))


for _ in range(int(input())):
    input()
    m = re.fullmatch(r"(\d*)([a-z]*)", input())
    if not m:
        print("NO")
        continue
    digits, letters = m.groups()
    print("YES" if is_sorted(digits) and is_sorted(letters) else "NO")
