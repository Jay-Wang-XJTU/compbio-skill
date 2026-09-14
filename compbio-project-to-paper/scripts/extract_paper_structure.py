#!/usr/bin/env python3
"""Extract a compact structural index from one or more scientific PDFs.

The output is intentionally an index rather than a full-text dump. It helps an
agent locate abstracts, section headings, figure/table captions, and candidate
pages for visual inspection without treating text extraction as layout review.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError as exc:  # pragma: no cover - environment guard
    raise SystemExit("Missing dependency: pypdf. Install with `python -m pip install pypdf`.") from exc


DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)
CAPTION_RE = re.compile(
    r"^(?:Fig(?:ure)?\.?|Extended Data Fig(?:ure)?\.?|Table|Supplementary Fig(?:ure)?\.?)\s*\d+[A-Za-z]?\b",
    re.IGNORECASE,
)
HEADING_RE = re.compile(
    r"^(?:abstract|introduction|results?|discussion|methods?|materials and methods|"
    r"conclusions?|limitations?|data availability|code availability|references|"
    r"supplementary information|acknowledg(?:e)?ments?)$",
    re.IGNORECASE,
)


def clean_line(line: str) -> str:
    return " ".join(line.replace("\u00ad", "").split())


def clipped(text: str, limit: int) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def collect_abstract(lines: list[str]) -> str:
    for index, line in enumerate(lines):
        if line.casefold() == "abstract" or line.casefold().startswith("abstract "):
            captured: list[str] = []
            remainder = line[8:].strip()
            if remainder:
                captured.append(remainder)
            for candidate in lines[index + 1 :]:
                if candidate.casefold() in {"introduction", "results", "main"}:
                    break
                captured.append(candidate)
                if sum(len(item) for item in captured) >= 2200:
                    break
            return clipped(" ".join(captured), 2200)
    return ""


def title_candidates(first_page_lines: list[str]) -> list[str]:
    candidates: list[str] = []
    for line in first_page_lines[:35]:
        if not 20 <= len(line) <= 240:
            continue
        if DOI_RE.search(line) or CAPTION_RE.match(line) or HEADING_RE.match(line):
            continue
        if re.fullmatch(r"[\d\W_]+", line):
            continue
        candidates.append(line)
        if len(candidates) == 4:
            break
    return candidates


def extract_pdf(path: Path, max_captions: int) -> dict[str, object]:
    reader = PdfReader(str(path))
    page_lines: list[list[str]] = []
    page_texts: list[str] = []

    for page in reader.pages:
        text = page.extract_text() or ""
        lines = [clean_line(line) for line in text.splitlines()]
        lines = [line for line in lines if line]
        page_lines.append(lines)
        page_texts.append("\n".join(lines))

    all_lines = [line for lines in page_lines for line in lines]
    front_text = "\n".join(page_texts[:3])
    doi_candidates = sorted({match.rstrip(".,;)") for match in DOI_RE.findall(front_text)})

    headings: list[dict[str, object]] = []
    captions: list[dict[str, object]] = []
    for page_number, lines in enumerate(page_lines, start=1):
        for line in lines:
            if HEADING_RE.fullmatch(line):
                item = {"page": page_number, "text": line}
                if item not in headings:
                    headings.append(item)
            if CAPTION_RE.match(line) and len(captions) < max_captions:
                captions.append({"page": page_number, "text": clipped(line, 700)})

    metadata = reader.metadata or {}
    return {
        "file": str(path.resolve()),
        "pages": len(reader.pages),
        "pdf_metadata_title": str(metadata.get("/Title") or "").strip(),
        "title_candidates": title_candidates(page_lines[0] if page_lines else []),
        "doi_candidates": doi_candidates[:5],
        "abstract": collect_abstract(all_lines),
        "headings": headings[:80],
        "captions": captions,
        "caption_pages": sorted({int(item["page"]) for item in captions}),
    }


def expand_inputs(values: list[str]) -> list[Path]:
    paths: list[Path] = []
    for value in values:
        candidate = Path(value)
        if candidate.is_dir():
            paths.extend(sorted(candidate.glob("*.pdf")))
        elif candidate.is_file():
            paths.append(candidate)
        else:
            raise FileNotFoundError(value)
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inputs", nargs="+", help="PDF files or directories containing PDFs")
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout")
    parser.add_argument("--max-captions", type=int, default=40)
    args = parser.parse_args()

    try:
        paths = expand_inputs(args.inputs)
        result = [extract_pdf(path, args.max_captions) for path in paths]
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    payload = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
