# ruff: noqa: E731, E741
def check(w, h, sx, sy, d):
    if sx - d <= 1 and sy - d <= 1:
        return False
    if sx + d >= w and sy + d >= h:
        return False
    if sx - d <= 1 and sx + d >= w:
        return False
    if sy - d <= 1 and sy + d >= h:
        return False
    return True


for _ in range(int(input())):
    w, h, sx, sy, d = map(int, input().split())
    print(h + w - 2 if check(w, h, sx, sy, d) else -1)
