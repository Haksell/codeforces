# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())

s = {0: 0, 1: 1, 2: 5, 5: 2, 8: 8}
VALID = "01258"


def f(hh, mm):
    if any(d not in VALID for d in str(hh) + str(mm)):
        return False
    a1 = s[hh // 10]
    a2 = s[hh % 10]
    a3 = s[mm // 10]
    a4 = s[mm % 10]
    return 10 * a4 + a3 < h and 10 * a2 + a1 < m


for _ in rir():
    h, m = mir()
    hh, mm = map(int, read().split(":"))
    while True:
        if f(hh, mm):
            print(f"{hh:02}:{mm:02}")
            break
        mm += 1
        if mm == m:
            mm = 0
            hh += 1
            if hh == h:
                hh = 0
