# ruff: noqa: E731, E741
for _ in range(int(input())):
    s = input()
    stack = []
    for c in s:
        if not stack or c == stack[-1]:
            stack.append(c)
        elif c != stack[-1]:
            stack.pop()
    moves = len(s) - len(stack) >> 1
    print("DA" if moves & 1 else "NET")
