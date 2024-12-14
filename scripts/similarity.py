import argparse
import os
import pickle
from rapidfuzz import fuzz
from itertools import combinations
from multiprocessing import Pool
import pyperclip

DIR = "problems"
CACHE_FILE = "scripts/similarities.pkl"
CACHE_SIZE = 1000

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
    ("1339A", "1422A"),
    ("1844A", "2009A"),
    ("1482A", "2009A"),
    ("1421A", "2009A"),
    ("1422A", "1956B"),
    ("1902A", "1972B"),
    ("1339A", "1956B"),
    ("1335A", "1968A"),
    ("1566A", "1646A"),
    ("0630C", "2010B"),
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


def recompute_similarities():
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
    results.sort(reverse=True)
    pickle.dump(results[:CACHE_SIZE], open(CACHE_FILE, "wb"))
    print(f"Saved to {CACHE_FILE}")
    return results


def get_similarities_cache():
    print(f"Loaded {CACHE_FILE}")
    return pickle.load(open(CACHE_FILE, "rb"))


def find_similarities(recompute):
    results = (
        recompute_similarities()
        if recompute or not os.path.exists(CACHE_FILE)
        else get_similarities_cache() or recompute_similarities()
    )
    return [
        (similarity, pair)
        for similarity, pair in results
        if problems(pair) not in DIFFERENT
    ]


def url(filename):
    contest = int(filename[len(DIR) + 1 : len(DIR) + 5])
    problem = filename[len(DIR) + 5 : -3]
    return f"https://codeforces.com/contest/{contest}/problem/{problem}"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recompute", action="store_true")
    return parser.parse_args()


def main():
    args = parse_args()
    similarities = find_similarities(args.recompute)
    similarity, pair = max(similarities)
    file1, file2 = pair
    pyperclip.copy(f"{repr(problems(pair))},")
    print(f"{file1}: {url(file1)}")
    print(f"{file2}: {url(file2)}")
    print(f"Similarity: {similarity:.3f}")
    os.system(f"code {file1}")
    os.system(f"code {file2}")


if __name__ == "__main__":
    main()
