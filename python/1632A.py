# ruff: noqa: E731, E741
for _ in range(int(input())):
    input()
    s = input()
    print("YES" if s == "0" or s == "1" or s == "01" or s == "10" else "NO")
