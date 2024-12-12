# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    z = 0
    for c in reversed(s):
        if c == "Q":
            z -= 1
            if z < 0:
                print("No")
                break
        else:
            z += 1
    else:
        print("Yes")
