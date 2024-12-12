# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().strip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        ax, ay = mir()
        bx, by = mir()
        cx, cy = mir()
        bx -= ax
        by -= ay
        cx -= ax
        cy -= ay
        px = min(abs(bx), abs(cx)) if (bx > 0) == (cx > 0) else 0
        py = min(abs(by), abs(cy)) if (by > 0) == (cy > 0) else 0
        print(px + py + 1)


if __name__ == "__main__":
    main()
