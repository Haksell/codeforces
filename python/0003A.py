# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def parse_line():
    x, y = map(ord, input())
    x -= 97
    y -= 48
    return x, y


def main():
    x1, y1 = parse_line()
    x2, y2 = parse_line()
    moves = []
    while x1 != x2 or y1 != y2:
        move = ""
        if x1 < x2:
            move += "R"
            x1 += 1
        elif x1 > x2:
            move += "L"
            x1 -= 1
        if y1 < y2:
            move += "U"
            y1 += 1
        elif y1 > y2:
            move += "D"
            y1 -= 1
        moves.append(move)
    print(len(moves))
    for move in moves:
        print(move)


if __name__ == "__main__":
    main()
