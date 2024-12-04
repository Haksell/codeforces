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
        s = input()
        if any(s.endswith(end) for end in ("ch", "x", "s", "o")):
            print(s + "es")
        elif any(s.endswith(end) for end in ("f", "fe")):
            print(s[: s.rindex("f")] + "ves")
        elif s.endswith("y"):
            print(s[:-1] + "ies")
        else:
            print(s + "s")


if __name__ == "__main__":
    main()
