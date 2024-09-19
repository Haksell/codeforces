for _ in range(int(input())):
    print(
        "TRIANGLE"
        if any([input().count("1") == 1 for _ in range(int(input()))])
        else "SQUARE"
    )
