# ruff: noqa: E731, E741
for _ in range(int(input())):
    n = int(input())
    s = input()
    if all(c == "1" for c in s):
        print("DRAW")
    elif n & 1 and s[n >> 1] == "0":
        print("BOB" if s.count("0") == 1 else "ALICE")
    else:
        print("BOB")
