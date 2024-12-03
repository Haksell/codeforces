# ruff: noqa: E731, E741
from collections import defaultdict
import random
import sys

read = sys.stdin.readline
input = lambda: read().rstrip()
ir = lambda: int(read())
rir = lambda: range(int(read()))
mir = lambda: map(int, read().split())
lmir = lambda: list(map(int, read().split()))


class AVLMultiSet:
    class Node:
        def __init__(self, key):
            self.key = key
            self.height = 1
            self.count = 1
            self.left = self.right = None
            self.left_len = self.right_len = 0

        def __len__(self):
            return self.left_len + self.count + self.right_len

        def __iter__(self):
            if self.left:
                yield from self.left
            for _ in range(self.count):
                yield self.key
            if self.right:
                yield from self.right

        def unique(self):
            if self.left:
                yield from self.left.unique()
            yield self.key
            if self.right:
                yield from self.right.unique()

        def __contains__(self, key):
            return self._count(key) >= 1

        def __getitem__(self, idx):
            if idx < self.left_len:
                return self.left[idx]
            elif idx < self.left_len + self.count:
                return self.key
            else:
                return self.right[idx - self.left_len - self.count]

        @property
        def left_height(self):
            return self.left.height if self.left else 0

        @property
        def right_height(self):
            return self.right.height if self.right else 0

        @property
        def balance(self):
            return self.left_height - self.right_height

        def _update(self):
            self.left_len = len(self.left) if self.left else 0
            self.right_len = len(self.right) if self.right else 0
            self.height = 1 + max(self.left_height, self.right_height)

        def _update_and_balance(self):
            self._update()
            balance = self.balance
            if balance > 1:
                if self.left and self.left.balance >= 0:  # Left Left
                    return self._rotate_right()
                else:  # Left Right
                    self.left = self.left._rotate_left()
                    return self._rotate_right()
            elif balance < -1:
                if self.right and self.right.balance <= 0:  # Right Right
                    return self._rotate_left()
                else:  # Right Left
                    self.right = self.right._rotate_right()
                    return self._rotate_left()
            else:
                return self

        def _rotate_left(self):
            parent, self.right.left, self.right = self.right, self, self.right.left
            self._update()
            parent._update()
            return parent

        def _rotate_right(self):
            parent, self.left.right, self.left = self.left, self, self.left.right
            self._update()
            parent._update()
            return parent

        def _count(self, key):
            if key < self.key:
                return self.left._count(key) if self.left else 0
            elif key > self.key:
                return self.right._count(key) if self.right else 0
            else:
                return self.count

    def __init__(self):
        self.root = None

    def __bool__(self):
        return self.root is not None

    def __len__(self):
        return len(self.root) if self.root else 0

    def __contains__(self, key):
        return key in self.root if self.root else False

    def __iter__(self):
        if self.root is None:
            return
        yield from self.root

    def unique(self):
        if self.root is None:
            return
        yield from self.root.unique()

    def __getitem__(self, idx):
        if idx >= len(self) or idx < -len(self):
            raise IndexError(f"{self.__class__.__name__} index out of range")
        return self.root[idx] if idx >= 0 else self.root[idx + len(self.root)]

    def __repr__(self):
        def inorder(node, depth):
            return (
                inorder(node.left, depth + 1)
                + [
                    "  " * depth
                    + f"{node.key}: {node.left_len} < {node.count} > {node.right_len}"
                ]
                + inorder(node.right, depth + 1)
                if node
                else []
            )

        return (
            "\n".join(inorder(self.root, 0))
            if self.root
            else f"{self.__class__.__name__}()"
        )

    def insert(self, key):
        self.root = self.__insert(self.root, key)

    def __insert(self, node, key):
        if node is None:
            return self.Node(key)
        if key == node.key:
            node.count += 1
            return node
        if key < node.key:
            node.left = self.__insert(node.left, key)
        else:
            node.right = self.__insert(node.right, key)
        return node._update_and_balance()

    def delete(self, key):
        self.root = self.__delete(self.root, key)

    def __delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self.__delete(node.left, key)
        elif key > node.key:
            node.right = self.__delete(node.right, key)
        elif node.count > 1:
            node.count -= 1
            return node
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key = successor.key
            node.count = successor.count
            successor.count = 1  # reset successor count to 1 to delete it
            node.right = self.__delete(node.right, successor.key)
        return node._update_and_balance()

    def count(self, key):
        return self.root._count(key) if self.root else 0

    def smaller_than(self, key):
        res = 0
        node = self.root
        while node:
            if node.key >= key:
                node = node.left
            else:
                res += node.count + node.left_len
                node = node.right
        return res


def main():
    for _ in rir():
        fuzz = random.randint(1, 1 << 30)
        points = defaultdict(list)
        left = AVLMultiSet()
        right = AVLMultiSet()
        for _ in rir():
            x, y = mir()
            points[x + fuzz].append(y)
            right.insert(y)
        unique_ys = list(right.unique())
        best_min = best_x = best_y = 0
        for x, ys in sorted(points.items()):
            lo = 1
            hi = len(unique_ys) - 1
            while lo <= hi:
                mi = lo + hi >> 1
                y = unique_ys[mi]
                bl = left.smaller_than(y)
                tl = len(left) - bl
                br = right.smaller_than(y)
                tr = len(right) - br
                m = min(bl, tl, br, tr)
                if m > best_min:
                    best_min = m
                    best_x = x - fuzz
                    best_y = y
                if min(bl, br) < min(tl, tr):
                    lo = mi + 1
                else:
                    hi = mi - 1
            for y in ys:
                left.insert(y)
                right.delete(y)
        print(best_min)
        print(best_x, best_y)


if __name__ == "__main__":
    main()
