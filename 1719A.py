# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, w = map(int, input().split())
    print("Burenka" if (h ^ w) & 1 else "Tonya")
