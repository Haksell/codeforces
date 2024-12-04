# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def inversions(lst):
    if len(lst) <= 1:
        return lst, 0

    mid = len(lst) >> 1
    left, left_inv = inversions(lst[:mid])
    right, right_inv = inversions(lst[mid:])
    res = left_inv + right_inv
    merged = []
    lidx = ridx = 0
    while lidx < len(left) and ridx < len(right):
        if left[lidx] <= right[ridx]:
            merged.append(left[lidx])
            lidx += 1
        else:
            res += len(left) - lidx
            merged.append(right[ridx])
            ridx += 1
    merged.extend(left[lidx:])
    merged.extend(right[ridx:])
    return merged, res


def main():
    read()
    a = lmir()
    _, inv = inversions(a)
    print(inv)


if __name__ == "__main__":
    main()
