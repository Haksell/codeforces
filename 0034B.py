_, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
print(sum(max(-n, 0) for n in a[:m]))
