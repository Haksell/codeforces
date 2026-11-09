from itertools import product
import math

pure_binaries = [int("".join(p)) for p in product("01", repeat=5)][2:]
all_binaries = cur_binaries = set(pure_binaries)
while cur_binaries:
    cur_binaries = {
        xy
        for xy in map(math.prod, product(pure_binaries, cur_binaries))
        if xy <= 100_000 and xy not in all_binaries
    }
    all_binaries |= cur_binaries
all_binaries.add(1)

for _ in range(int(input())):
    print("YES" if int(input()) in all_binaries else "NO")
