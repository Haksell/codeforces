for _ in range(int(input())):
    rating = int(input())
    division = 4 if rating < 1400 else 3 if rating < 1600 else 2 if rating < 1900 else 1
    print(f"Division {division}")