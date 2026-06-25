# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def query(x):
    print(x, flush=True)
    return ir() == 1


def solve():
    n = ir()
    query("mul 9")
    query("digit")
    query("digit")
    query(f"add {n - 9}")
    query("!")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
