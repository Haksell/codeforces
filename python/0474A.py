# ruff: noqa: E731, E741
keyboard = """\
qwertyuiop
asdfghjkl;
zxcvbnm,./"""

d = input()
s = input()
if d == "L":
    print("".join(keyboard[keyboard.index(c) + 1] for c in s))
else:
    print("".join(keyboard[keyboard.index(c) - 1] for c in s))
