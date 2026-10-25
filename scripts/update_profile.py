"""Refresh the merged-pull-request table in the profile README.

The table between the MERGED markers is generated from the GitHub search API,
so the profile page does not sit stale for months after a PR lands.
"""

from __future__ import annotations

import json
import os
import re
import urllib.parse
import urllib.request

README = "README.md"
START = "<!-- MERGED:START -->"
END = "<!-- MERGED:END -->"
TOKEN = os.environ["GH_TOKEN"]
USER = os.environ.get("PROFILE_USER", "Duo-ee")
LIMIT = int(os.environ.get("MERGED_LIMIT", "8"))


def api(path: str, params: dict[str, str] | None = None) -> dict:
    url = "https://api.github.com" + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"token {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "profile-updater",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def merged_prs() -> list[dict[str, str]]:
    data = api(
        "/search/issues",
        {
            "q": f"is:pr is:merged author:{USER}",
            "sort": "updated",
            "order": "desc",
            "per_page": str(LIMIT),
        },
    )
    pairs: list[dict[str, str]] = []
    for item in data.get("items", []):
        parts = item["repository_url"].rsplit("/", 2)
        pairs.append(
            {
                "repo": f"{parts[-2]}/{parts[-1]}",
                "number": str(item["number"]),
                "title": item["title"],
            }
        )
    return pairs


def shorten(title: str, width: int = 72) -> str:
    if len(title) <= width:
        return title
    return title[: width - 3].rstrip() + "..."


def render(prs: list[dict[str, str]]) -> str:
    if not prs:
        return "_Nothing merged yet._"
    lines = ["| Repository | PR | Change |", "|:--|:--|:--|"]
    for pr in prs:
        repo = pr["repo"]
        number = pr["number"]
        lines.append(
            f"| [{repo}](https://github.com/{repo}) "
            f"| [#{number}](https://github.com/{repo}/pull/{number}) "
            f"| {shorten(pr['title'])} |"
        )
    return "\n".join(lines)


def main() -> None:
    block = render(merged_prs())
    text = open(README, encoding="utf-8").read()
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END), re.DOTALL
    )
    if pattern.search(text) is None:
        raise SystemExit("MERGED markers not found in README.md")
    updated = pattern.sub(lambda _: f"{START}\n{block}\n{END}", text, count=1)
    if updated == text:
        print("no change")
        return
    with open(README, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(updated)
    print(f"updated with {block.count(chr(10)) - 1} merged PRs")


if __name__ == "__main__":
    main()
