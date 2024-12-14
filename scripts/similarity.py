from heapq import nlargest
import os
from rapidfuzz import fuzz
from itertools import combinations
from multiprocessing import Pool

DIR = "problems"


def compare_files(pair):
    file1, file2 = pair
    return (fuzz.ratio(contents[file1], contents[file2]), file1, file2)


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

    file_pairs = list(combinations(filenames, 2))
    with Pool() as pool:
        results = pool.map(compare_files, file_pairs)
    return results


def url(filename):
    contest = int(filename[len(DIR) + 1 : len(DIR) + 5])
    problem = filename[len(DIR) + 5 : -3]
    return f"https://codeforces.com/contest/{contest}/problem/{problem}"


def main():
    similarities = find_similarities()
    for i, (similarity, file1, file2) in enumerate(nlargest(3, similarities)):
        if i:
            print()
        print(f"{file1}: {url(file1)}")
        print(f"{file2}: {url(file2)}")
        print(f"Similarity: {similarity:.3f}")


if __name__ == "__main__":
    main()
