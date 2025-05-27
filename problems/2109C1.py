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
    query("digit")  # 1-81
    query("digit")  # 1-16
    query("add -8")
    query("add -4")
    query("add -2")
    query("add -1")
    query(f"add {n - 1}")
    query("!")


def main():
    for _ in rir():
        solve()


if __name__ == "__main__":
    main()
