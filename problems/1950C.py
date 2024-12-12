# ruff: noqa: E731, E741
for _ in range(int(input())):
    h, m = map(int, input().split(":"))
    x = "AM" if h < 12 else "PM"
    h = h % 12 or 12
    print(f"{h:02}:{m:02} {x}")
