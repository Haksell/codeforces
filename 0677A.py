_, h = map(int, input().split())
print(sum(1 if n <= h else 2 for n in map(int, input().split())))
