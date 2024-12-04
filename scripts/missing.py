#!/usr/bin/env python

from dataclasses import dataclass
import os
import requests


@dataclass
class Submission:
    id: int
    creation_time: int
    contest: int
    problem: str


def get_repo():
    return {file[:-3] for file in os.listdir() if file.endswith(".py")}


def get_accepted():
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

    return accepted


def main():
    repo = get_repo()
    accepted = get_accepted()
    present_but_unsolved = sorted(repo - set(accepted))
    if present_but_unsolved:
        print(
            "Problems in repo that are not marked as accepted on codeforces:",
            *present_but_unsolved,
        )
        return
    print("OK")
    # for problem_id, submission in accepted.items():
    #     print(problem_id, submission)
    #     print(
    #         f"https://codeforces.com/contest/{submission.contest}/submission/{submission.id}"
    #     )


if __name__ == "__main__":
    main()
