# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def main():
    for _ in rir():
        h, w = mir()
        s1 = " ".join("1" if x & 3 in (1, 2) else "0" for x in range(w))
        s2 = "".join("0" if c == "1" else "1" if c == "0" else " " for c in s1)
        for y in range(h):
            print(s1 if y & 3 in (1, 2) else s2)


if __name__ == "__main__":
    main()
