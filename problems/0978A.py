# ruff: noqa: E731, E741
input()
a = list(map(int, input().split()))
b = []
s = set()
for n in reversed(a):
    if n not in s:
        s.add(n)
        b.append(n)
print(len(b))
print(*reversed(b))
