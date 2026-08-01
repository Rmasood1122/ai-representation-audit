#!/usr/bin/env python3
"""
verify_provenance.py — Programmatic Provenance Ingestion Gate (Document 1.1, Section 3.2)

Implements the DEV-001 corrective action: no extraction claim may be marked
complete unless the raw payloads are physically present, parse cleanly, and
every claimed character span matches the raw source text exactly.

Exit code 0  => GATE PASS (all assertions hold; hashes written to manifest)
Exit code 1  => GATE FAIL (any assertion violated; failures listed)
Exit code 2  => GATE FAIL (required files missing / unreadable — the DEV-001 mode)

Usage:
    python3 verify_provenance.py <capture_dir>

Expected contents of <capture_dir>:
    api_capture.json        raw API JSON payload, byte-for-byte as received
    ui_capture.txt          raw UI answer text, UTF-8, as copied
    extraction_manifest.json  the S1 claim under test, shape:
    {
      "prompt": "...",
      "api": {
        "engine": "...", "model": "...", "timestamp_utc": "...",
        "request_id": "...",
        "answer_json_path": ["choices", 0, "message", "content"],
        "entities": [ {"surface": "Snowflake", "start": 138, "end": 147}, ... ]
      },
      "ui": {
        "engine": "...", "timestamp_utc": "...", "locale": "...",
        "web_search_active": true,
        "entities": [ {"surface": "Snowflake", "start": 142, "end": 151}, ... ]
      }
    }
Spans are half-open UTF-8 character offsets [start, end) into the source text.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

REQUIRED_FILES = ["api_capture.json", "ui_capture.txt", "extraction_manifest.json"]
# Sanity shape only. A real provider request id is req_ + opaque token, with no
# embedded provider names or dates. This catches lazy forgeries, not clever ones;
# true authenticity lives with the provider's logs (Section 3.2).
REQUEST_ID_RE = re.compile(r"^req_[A-Za-z0-9]{8,}$")
FORGERY_HINTS = ("openai", "anthropic", "google", "202")  # substrings that should not appear in an opaque id


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def walk_json_path(obj, path):
    for key in path:
        obj = obj[key] if isinstance(key, str) else obj[int(key)]
    return obj


def check_spans(label, source_text, entities, failures):
    if not entities:
        failures.append(f"{label}: entity list is empty — an extraction claim with no entities is not a completed S1")
        return
    for i, ent in enumerate(entities):
        surface, start, end = ent.get("surface"), ent.get("start"), ent.get("end")
        if surface is None or start is None or end is None:
            failures.append(f"{label}[{i}]: missing surface/start/end")
            continue
        if not (0 <= start < end <= len(source_text)):
            failures.append(
                f"{label}[{i}] '{surface}': span [{start},{end}) outside source length {len(source_text)}"
            )
            continue
        actual = source_text[start:end]
        if actual != surface:
            failures.append(
                f"{label}[{i}]: claimed '{surface}' but source[{start}:{end}] is '{actual}' — SPAN MISMATCH"
            )


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1
    capture_dir = Path(sys.argv[1])
    failures, missing = [], []

    # --- Assertion 0: physical presence (the DEV-001 gate) ---
    for name in REQUIRED_FILES:
        if not (capture_dir / name).is_file():
            missing.append(name)
    if missing:
        print("GATE FAIL [DEV-001 MODE]: required raw payload files are absent:")
        for m in missing:
            print(f"  MISSING: {capture_dir / m}")
        print("No claim of verification is valid without the underlying raw files.")
        return 2

    # --- Assertion 1: files parse ---
    try:
        manifest = json.loads((capture_dir / "extraction_manifest.json").read_text(encoding="utf-8"))
    except Exception as e:
        print(f"GATE FAIL: extraction_manifest.json does not parse: {e}")
        return 2
    try:
        api_raw = json.loads((capture_dir / "api_capture.json").read_text(encoding="utf-8"))
    except Exception as e:
        print(f"GATE FAIL: api_capture.json does not parse as JSON: {e}")
        return 2
    ui_text = (capture_dir / "ui_capture.txt").read_text(encoding="utf-8")
    if not ui_text.strip():
        print("GATE FAIL: ui_capture.txt is empty")
        return 2

    # --- Assertion 2: API answer text extractable at declared path ---
    api_cfg = manifest.get("api", {})
    try:
        api_text = walk_json_path(api_raw, api_cfg.get("answer_json_path", []))
        assert isinstance(api_text, str) and api_text.strip()
    except Exception:
        failures.append("api: answer_json_path does not resolve to non-empty text inside api_capture.json")
        api_text = ""

    # --- Assertion 3: span traceability, both arms ---
    if api_text:
        check_spans("A* (api)", api_text, api_cfg.get("entities", []), failures)
    check_spans("U* (ui)", ui_text, manifest.get("ui", {}).get("entities", []), failures)

    # --- Assertion 4: metadata sanity ---
    rid = api_cfg.get("request_id", "")
    if not REQUEST_ID_RE.match(rid):
        failures.append(f"api.request_id '{rid}' fails shape check (expect 'req_' + opaque token)")
    else:
        lowered = rid.lower()
        hints = [h for h in FORGERY_HINTS if h in lowered]
        if hints:
            failures.append(
                f"api.request_id '{rid}' embeds {hints} — real ids are opaque; flagged as probable fabrication"
            )
    for arm in ("api", "ui"):
        if not manifest.get(arm, {}).get("timestamp_utc"):
            failures.append(f"{arm}.timestamp_utc missing")

    # --- Verdict ---
    if failures:
        print(f"GATE FAIL: {len(failures)} assertion(s) violated:")
        for f in failures:
            print(f"  - {f}")
        return 1

    hashes = {name: sha256_file(capture_dir / name) for name in REQUIRED_FILES}
    manifest["_provenance_gate"] = {"status": "PASS", "sha256": hashes}
    (capture_dir / "extraction_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    print("GATE PASS: all assertions hold. SHA-256 of raw payloads:")
    for name, digest in hashes.items():
        print(f"  {name}: {digest}")
    print("S1 may now be marked EXECUTED; these hashes enter the append-only chain.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
