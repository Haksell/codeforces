# ruff: noqa: E731, E741
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


def inversions(lst, lo, hi):
    if lo + 1 == hi:
        return [lst[lo]], 0

    mi = lo + hi >> 1
    left, left_inv = inversions(lst, lo, mi)
    right, right_inv = inversions(lst, mi, hi)
    res = left_inv + right_inv
    merged = [0] * len(left) + len(right)
    lidx = ridx = 0
    while lidx < len(left) and ridx < len(right):
        if left[lidx] <= right[ridx]:
            merged[lidx + ridx] = left[lidx]
            lidx += 1
        else:
            res += len(left) - lidx
            merged[lidx + ridx] = right[ridx]
            ridx += 1
    for i in range(lidx, len(left)):
        merged[lidx + ridx] = left[i]
    for i in range(ridx, len(right)):
        merged[lidx + ridx] = right[i]
    return merged, res


def main():
    n = ir()
    a = lmir()
    _, inv = inversions(a, 0, n)
    print(inv)


if __name__ == "__main__":
    main()
