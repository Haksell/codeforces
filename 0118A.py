VOWELS = "aeiouy"
print("".join("." + c for c in input().lower() if c not in VOWELS))
