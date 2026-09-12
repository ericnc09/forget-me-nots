"""Search Exa with auto retrieval and query-relevant highlights."""

import argparse
import json
import os
from pathlib import Path
import sys
from typing import Any

from dotenv import load_dotenv
from exa_py import Exa
from requests.exceptions import RequestException


def search(
    query: str,
    *,
    num_results: int = 10,
    include_domains: list[str] | None = None,
    max_age_hours: int | None = None,
) -> dict[str, Any]:
    """Return titles, source URLs, and highlights for use in an agent loop.

    Loads .env beside this file; an existing environment variable takes priority.
    Freshness uses Exa's default behavior unless max_age_hours is supplied.
    """
    if not query.strip():
        raise ValueError("The search query cannot be empty.")
    if not 1 <= num_results <= 100:
        raise ValueError("num_results must be between 1 and 100.")
    if max_age_hours is not None and max_age_hours < -1:
        raise ValueError("max_age_hours must be -1 or a nonnegative integer.")

    load_dotenv(Path(__file__).resolve().with_name(".env"), override=False)
    api_key = os.environ.get("EXA_API_KEY", "").strip()
    if not api_key or api_key == "YOUR_API_KEY":
        raise ValueError(
            "Set EXA_API_KEY in your environment or in exa-search/.env before searching."
        )

    contents: dict[str, Any] = {"highlights": True}
    if max_age_hours is not None:
        contents["max_age_hours"] = max_age_hours

    response = Exa(api_key=api_key).search(
        query.strip(),
        type="auto",
        num_results=num_results,
        include_domains=include_domains,
        contents=contents,
    )
    return {
        "results": [
            {
                "title": result.title,
                "url": result.url,
                "highlights": result.highlights or [],
            }
            for result in response.results
        ]
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="Natural language search query")
    parser.add_argument("--num-results", type=int, default=10, metavar="N")
    parser.add_argument(
        "--include-domain", action="append", dest="include_domains",
        metavar="DOMAIN", help="Restrict sources; repeat for multiple domains",
    )
    parser.add_argument(
        "--max-age-hours", type=int, metavar="HOURS",
        help="0 always crawls; -1 uses cache only; omitted uses Exa's default",
    )
    args = parser.parse_args()
    try:
        result = search(
            args.query,
            num_results=args.num_results,
            include_domains=args.include_domains,
            max_age_hours=args.max_age_hours,
        )
    except (ValueError, RequestException) as exc:
        # Redact the configured key if a service error happens to echo it.
        message = str(exc)
        api_key = os.environ.get("EXA_API_KEY", "").strip()
        if api_key:
            message = message.replace(api_key, "[redacted]")
        print(f"Exa search failed: {message}", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
