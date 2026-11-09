for _ in range(int(input())):
    a, b, c = map(int, input().split())
    print("First" if a + (c & 1) > b else "Second")
