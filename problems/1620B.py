# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def best_triangle(height):
    line = lmir()[1:]
    return (max(line) - min(line)) * height


def main():
    for _ in rir():
        w, h = mir()
        print(
            max(
                best_triangle(h),
                best_triangle(h),
                best_triangle(w),
                best_triangle(w),
            )
        )


if __name__ == "__main__":
    main()
