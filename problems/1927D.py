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
        n = ir()
        a = lmir()
        prev_diff = [-1] * n
        for i in range(1, n):
            if a[i] == a[i - 1]:
                prev_diff[i] = prev_diff[i - 1]
            else:
                prev_diff[i] = i - 1
        for _ in rir():
            lo, hi = mir()
            lo -= 1
            hi -= 1
            prev = prev_diff[hi]
            if prev >= lo:
                print(prev + 1, hi + 1)
            else:
                print(-1, -1)


if __name__ == "__main__":
    main()
