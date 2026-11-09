# ruff: noqa: TRY002

import argparse
import os
import pickle
import sys
from dataclasses import dataclass

import requests

DIR_PYTHON = "python"
DIR_RUST = "src/bin"


@dataclass
class Submission:
    id: int
    creation_time: int
    contest: str
    problem: str


def get_repo():
    python_files = {
        file[:-3] for file in os.listdir(DIR_PYTHON) if file.endswith(".py")
    }
    rust_files = {file[:-3] for file in os.listdir(DIR_RUST) if file.endswith(".rs")}
    return python_files | rust_files


def get_accepted(recompute):
    ACCEPTED_FILE = "scripts/accepted.pkl"
    if not recompute and os.path.exists(ACCEPTED_FILE):
        print(f"Loaded {ACCEPTED_FILE}")
        return pickle.load(open(ACCEPTED_FILE, "rb"))

    url = "https://codeforces.com/api/user.status?handle=Haksell"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    data = response.json()
    if data["status"] != "OK":
        raise Exception(f"Error in response: {data['comment']}")

    accepted = {}
    for submission in data["result"]:
        if submission["verdict"] != "OK":
            continue
        if "contestId" in submission:
            contest = str(submission["problem"]["contestId"]).zfill(4)
            problem = submission["problem"]["index"]
            problem_id = f"{contest:04}{problem}"
        else:
            assert submission["problem"]["problemsetName"] == "acmsguru"
            contest = "ACM"
            problem = submission["problem"]["index"]
            problem_id = f"{contest}{problem}"
        creation_time = submission["creationTimeSeconds"]
        if (
            problem_id not in accepted
            or creation_time > accepted[problem_id].creation_time
        ):
            accepted[problem_id] = Submission(
                submission["id"], creation_time, contest, problem
            )

    pickle.dump(accepted, open(ACCEPTED_FILE, "wb"))  # noqa: SIM115
    return accepted


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--recompute", action="store_true")
    return parser.parse_args()


def handle_unsolved(repo, accepted):
    present_but_unsolved = sorted(repo - set(accepted))
    if present_but_unsolved:
        print(
            "Problems in repo that are not marked as accepted on codeforces:",
            *present_but_unsolved,
        )
        sys.exit()


def handle_solved(repo, accepted):
    cnt = 0
    for problem_id, submission in sorted(accepted.items()):
        if problem_id in repo:
            continue
        url = (
            f"https://codeforces.com/problemsets/acmsguru/submission/99999/{submission.id}"
            if submission.contest == "ACM"
            else f"https://codeforces.com/contest/{submission.contest}/submission/{submission.id}"
        )
        print(url)
        cnt += 1
    if cnt == 0:
        print("Codeforces and GitHub are in sync.")
    else:
        print(f"{cnt} problem{'s' if cnt >= 2 else ''} remaining.")


def main():
    args = parse_args()
    repo = get_repo()
    accepted = get_accepted(args.recompute)
    handle_unsolved(repo, accepted)
    handle_solved(repo, accepted)


if __name__ == "__main__":
    main()
