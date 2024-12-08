# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    print("YES" if s.count("B") == s.count("A") + s.count("C") else "NO")
