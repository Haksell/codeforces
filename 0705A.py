# ruff: noqa: E731, E741
n = int(input())
print(" that ".join("I love" if i & 1 else "I hate" for i in range(n)) + " it")
