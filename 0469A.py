n = int(input())
s1 = set(list(map(int, input().split()))[1:])
s2 = set(list(map(int, input().split()))[1:])
if s1 | s2 == set(range(1, n + 1)):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
