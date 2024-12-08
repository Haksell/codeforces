# ruff: noqa: E731, E741
import sys


def popcount(n):
    return bin(n).count("1")


n, q = map(int, sys.stdin.readline().split())
a = [int(x) - 1 for x in sys.stdin.readline().split()]
t = [int(x) - 1 for x in sys.stdin.readline().split()]
ridx = [0] * 50
for i in reversed(range(n)):
    ridx[a[i]] = i
initial_masks = [0] * 50
mask = 0
for i, card in enumerate(a):
    if i == ridx[card]:
        initial_masks[card] = mask
        mask |= 1 << card
found = [False] * 50
ans = []
masks = initial_masks.copy()
for card in t:
    if found[card]:
        x = popcount(masks[card])
    else:
        x = ridx[card] + popcount(masks[card] & ~initial_masks[card])
        found[card] = True
    ans.append(str(x + 1))
    for i in range(50):
        masks[i] |= 1 << card
    masks[card] = 0
sys.stdout.write("\n".join(ans))
