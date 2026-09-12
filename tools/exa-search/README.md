# Exa search for Codex

A standalone Python helper for the supplied setup: `type="auto"`, 10 results,
and `contents={"highlights": True}`. It prints JSON containing source titles,
URLs, and excerpts. Codex can invoke it through the terminal, and Python agents
can import `search` from `exa_search`. This is a Python integration; it does not
register an MCP server or change global Codex settings.

## Setup

Requires Python 3.10 or newer. From this directory:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
```

Put your key from the [Exa dashboard](https://dashboard.exa.ai/api-keys) into
the local `.env` file as `EXA_API_KEY=your_actual_key`. Alternatively, set
`EXA_API_KEY` in the calling process's environment. Environment variables take
priority over `.env`; the helper loads `.env` beside its own file regardless of
the working directory. Local credentials and the virtual environment are ignored
by Git.

## Run

```sh
.venv/bin/python exa_search.py "Next.js route handler authentication example"
.venv/bin/python exa_search.py "Next.js authentication" --num-results 5 --include-domain nextjs.org
```

From the repository root:

```sh
tools/exa-search/.venv/bin/python tools/exa-search/exa_search.py \
  "Next.js route handler authentication example"
```

Freshness is optional: `--max-age-hours 24` allows a day-old cache,
`--max-age-hours 0` forces a crawl, and `--max-age-hours -1` uses cache only.
Omit it for Exa's default. Search requires an API key and network access.
Successful output goes to stdout; failures go to stderr with a nonzero exit code.

## Guide verification — September 12, 2026

The [current coding-agent reference](https://exa.ai/docs/reference/search-api-guide-for-coding-agents)
confirms the supplied `auto` search and highlights example. The originally
supplied `docs.exa.ai` URL could not be opened by the browsing tool; the matching
reference is available under `exa.ai/docs`.

- The pasted `exa-py==2.14.0` pin is older. This helper pins
  [2.20.0, released September 1, 2026](https://pypi.org/project/exa-py/2.20.0/).
- The reference now lists text verbosity `compact`, `standard`, and `full`;
  the pasted guide omits `standard`. Highlights also support an object with
  query and character-limit controls. Plain `highlights=True` remains valid.
- In the [official SDK source](https://github.com/exa-labs/exa-py/blob/master/exa_py/api.py),
  omitting search contents requests text by default. Use `contents=False`
  for URLs only. For known URLs and excerpts only, explicitly use
  `exa.get_contents(urls, highlights=True, text=False)` to suppress default text.
- Python uses snake_case, including nested options such as `max_age_hours`.
  Structured search uses `output_schema` and `system_prompt`; Python streaming
  uses `stream_search`. These features are outside this small retrieval helper.

The local virtual environment is installed. Dependency compatibility and CLI help
passed. Smoke checks using the installed SDK with mocked HTTP verified request
serialization, response parsing, empty results, missing credentials, and API-error
key redaction. No authenticated search was made; live API behavior still needs a
real key.
