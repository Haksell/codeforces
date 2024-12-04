#!/usr/bin/env python

import argparse
from dataclasses import dataclass
import os
import pickle
import sys
import requests


@dataclass
class Submission:
    id: int
    creation_time: int
    contest: int
    problem: str


def get_repo():
    return {file[:-3] for file in os.listdir() if file.endswith(".py")}


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

    accepted = dict()
    for submission in data["result"]:
        if submission["verdict"] == "OK" and "contestId" in submission:
            contest = submission["problem"]["contestId"]
            problem = submission["problem"]["index"]
            creation_time = submission["creationTimeSeconds"]
            problem_id = f"{contest:04}{problem}"
            if (
                problem_id not in accepted
                or creation_time > accepted[problem_id].creation_time
            ):
                accepted[problem_id] = Submission(
                    submission["id"], creation_time, contest, problem
                )

    pickle.dump(accepted, open(ACCEPTED_FILE, "wb"))
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
    for problem_id, submission in accepted.items():
        print(problem_id, submission)
        print(
            f"https://codeforces.com/contest/{submission.contest}/submission/{submission.id}"
        )
        break


def main():
    args = parse_args()
    repo = get_repo()
    accepted = get_accepted(args.recompute)
    handle_unsolved(repo, accepted)
    handle_solved(repo, accepted)


if __name__ == "__main__":
    main()
