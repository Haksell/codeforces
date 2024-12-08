# ruff: noqa: E731, E741
def dist(start, end, size):
    return end - start if end >= start else 2 * size - start - end


for _ in range(int(input())):
    h, w, ry, rx, dy, dx = map(int, input().split())
    print(min(dist(rx, dx, w), dist(ry, dy, h)))
