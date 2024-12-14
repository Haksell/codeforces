# ruff: noqa: E731, E741
s = input()
ab = [i for i in range(len(s) - 1) if s[i : i + 2] == "AB"]
ba = [i for i in range(len(s) - 1) if s[i : i + 2] == "BA"]
print("YES" if any(abs(i - j) >= 2 for i in ab for j in ba) else "NO")
