
import os
import time
from pathlib import Path

import requests


URL = "https://leetcode.com/graphql"
OUTPUT = Path("solutions")

USERNAME = os.environ["LEETCODE_USERNAME"]
SESSION = os.environ["LEETCODE_SESSION"]
CSRF = os.environ["LEETCODE_CSRF_TOKEN"]

LANGUAGES = {
    "python": "py",
    "python3": "py",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "csharp": "cs",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "rust": "rs",
    "kotlin": "kt",
    "swift": "swift",
    "ruby": "rb",
    "mysql": "sql",
    "mssql": "sql",
    "postgresql": "sql",
    "bash": "sh",
}

RECENT_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
    lang
  }
}
"""

DETAIL_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    runtimeDisplay
    memoryDisplay
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    titleSlug
  }
}
"""

class LeetCodeClient:
    def __init__(self):
        self.session = requests.Session()

        self.session.cookies.set(
            "LEETCODE_SESSION", SESSION,
            domain="leetcode.com"
        )
        self.session.cookies.set(
            "csrftoken", CSRF,
            domain="leetcode.com"
        )

        self.session.headers.update({
            "Content-Type": "application/json",
            "Referer": "https://leetcode.com",
            "x-csrftoken": CSRF,
            "User-Agent": "LeetCodeGitHubSync/1.0",
        })

    def query(self, query, variables):
        response = self.session.post(
            URL,
            json={
                "query": query,
                "variables": variables,
            },
            timeout=30,
        )

        response.raise_for_status()
        result = response.json()

        if result.get("errors"):
            raise RuntimeError(
                "LeetCode GraphQL query failed"
            )

        if not result.get("data"):
            raise RuntimeError(
                "LeetCode returned no data"
            )

        return result["data"]

    def get_accepted(self):
        data = self.query(
            RECENT_QUERY,
            {
                "username": USERNAME,
                "limit": 100,
            },
        )

        return data.get(
            "recentAcSubmissionList", []
        ) or []

    def get_code(self, submission_id):
        data = self.query(
            DETAIL_QUERY,
            {
                "submissionId": int(submission_id),
            },
        )

        details = data.get("submissionDetails")
        return details.get("code") if details else None
    
    def get_problem_number(self, title_slug):
        data = self.query(
            QUESTION_QUERY,
            {"titleSlug": title_slug},
        )
    
        question = data.get("question")
        if not question:
            raise RuntimeError(
                f"Could not retrieve problem: {title_slug}"
            )
    
        return question["questionFrontendId"]


def sync():
    client = LeetCodeClient()
    submissions = client.get_accepted()

    print(f"Found {len(submissions)} accepted submissions")

    added = 0
    problem_numbers = {}

    for submission in reversed(submissions):
        submission_id = str(submission["id"])
        slug = submission["titleSlug"]
        language = submission.get("lang", "unknown")

        extension = LANGUAGES.get(language, "txt")

        # Cache problem numbers to avoid repeated API calls.
        if slug not in problem_numbers:
            problem_numbers[slug] = (
                client.get_problem_number(slug)
            )
            time.sleep(1)

        problem_number = problem_numbers[slug]

        # Pad numeric problem IDs to four digits.
        formatted_number = (
            problem_number.zfill(4)
            if problem_number.isdigit()
            else problem_number
        )

        # submissions/0001-two-sum/python3/
        folder = (
            Path("submissions")
            / f"{formatted_number}-{slug}"
            / language
        )

        file_path = folder / f"{submission_id}.{extension}"

        # Don't download duplicates.
        if file_path.exists():
            continue

        code = client.get_code(submission_id)

        if not code:
            print(f"Skipping {submission_id}: no code")
            continue

        folder.mkdir(parents=True, exist_ok=True)
        file_path.write_text(
            code,
            encoding="utf-8",
        )

        print(f"Added: {file_path}")
        added += 1

        time.sleep(1)

    print(f"Sync complete. Added {added} solutions.")



if __name__ == "__main__":
    sync()
