# ruff: noqa: E731, E741
s = input()
h = len(s) >> 1
diff = sum(s[i] != s[~i] for i in range(h))
print("YES" if diff == 1 or (diff == 0 and len(s) & 1) else "NO")
