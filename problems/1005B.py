# ruff: noqa: E731, E741
s = input()[::-1]
t = input()[::-1]
i = next((i for i, (si, ti) in enumerate(zip(s, t)) if si != ti), min(len(s), len(t)))
print(len(s) + len(t) - 2 * i)
