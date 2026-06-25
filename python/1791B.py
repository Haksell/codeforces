# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    x = y = 0
    for c in input():
        if c == "U":
            y += 1
        elif c == "R":
            x += 1
        elif c == "D":
            y -= 1
        else:
            x -= 1
        if x == y == 1:
            print("YES")
            break
    else:
        print("NO")
