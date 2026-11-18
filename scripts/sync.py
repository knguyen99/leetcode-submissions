
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


def sync():
    client = LeetCodeClient()
    submissions = client.get_accepted()

    print(f"Found {len(submissions)} accepted submissions")

    added = 0

    for submission in reversed(submissions):
        submission_id = str(submission["id"])
        slug = submission["titleSlug"]
        language = submission.get("lang", "")

        extension = LANGUAGES.get(language, "txt")

        folder = OUTPUT / slug
        file_path = folder / f"{submission_id}.{extension}"

        # Skip submissions already saved.
        if file_path.exists():
            continue

        # Fetch the actual source code.
        code = client.get_code(submission_id)

        if not code:
            print(f"Skipping {submission_id}: code unavailable")
            continue

        folder.mkdir(parents=True, exist_ok=True)
        file_path.write_text(code, encoding="utf-8")

        print(f"Added: {slug}/{file_path.name}")
        added += 1

        # Avoid sending requests too quickly.
        time.sleep(1)

    print(f"Sync complete. Added {added} solutions.")


if __name__ == "__main__":
    sync()
