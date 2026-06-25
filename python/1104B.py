# ruff: noqa: E731, E741
stack = []
n = 0
for c in input():
    if stack and stack[-1] == c:
        stack.pop()
        n += 1
    else:
        stack.append(c)
print("Yes" if n & 1 == 1 else "No")
