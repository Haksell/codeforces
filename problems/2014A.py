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
        _, k = mir()
        a = lmir()
        res = money = 0
        for ai in a:
            if ai >= k:
                money += ai
            elif ai == 0 and money:
                money -= 1
                res += 1
        print(res)


if __name__ == "__main__":
    main()
