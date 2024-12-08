# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    r1 = input()
    r2 = input()
    print("YES" if all(c1 == "0" or c2 == "0" for c1, c2 in zip(r1, r2)) else "NO")
