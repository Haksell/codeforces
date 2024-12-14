import os
from rapidfuzz import fuzz
from itertools import combinations
from multiprocessing import Pool
import pyperclip

DIR = "problems"

DIFFERENT = {
    ("1370A", "1968A"),
    ("1420A", "1637A"),
    ("1421A", "1844A"),
    ("1421A", "1482A"),
    ("1422A", "1740A"),
    ("1455C", "1844A"),
    ("1455C", "1482A"),
    ("1482A", "1772A"),
    ("1482A", "1844A"),
    ("1772A", "1844A"),
    ("1878B", "1983A"),
    ("1421A", "1772A"),
    ("1421A", "1455C"),
    ("1335A", "1370A"),
}


def problems(file_pair):
    file1, file2 = file_pair
    problem1 = file1[len(DIR) + 1 : -3]
    problem2 = file2[len(DIR) + 1 : -3]
    return (problem1, problem2)


def compare_files(pair):
    file1, file2 = pair
    similarity = fuzz.ratio(contents[file1], contents[file2])
    return (similarity, pair)


def find_similarities():
    global contents
    contents = dict()
    filenames = []
    for filename in sorted(os.listdir(DIR)):
        if not filename.endswith(".py"):
            continue
        filename = os.path.join(DIR, filename)
        if os.path.islink(filename):
            continue
        filenames.append(filename)
        with open(filename) as f:
            contents[filename] = f.read()

    file_pairs = [
        pair for pair in combinations(filenames, 2) if problems(pair) not in DIFFERENT
    ]
    with Pool() as pool:
        results = pool.map(compare_files, file_pairs)
    return results


def url(filename):
    contest = int(filename[len(DIR) + 1 : len(DIR) + 5])
    problem = filename[len(DIR) + 5 : -3]
    return f"https://codeforces.com/contest/{contest}/problem/{problem}"


def main():
    similarities = find_similarities()
    similarity, pair = max(similarities)
    file1, file2 = pair
    pyperclip.copy(f"{repr(problems(pair))},")
    print(f"{file1}: {url(file1)}")
    print(f"{file2}: {url(file2)}")
    print(f"Similarity: {similarity:.3f}")


if __name__ == "__main__":
    main()
