#!/usr/bin/env python3
"""smoke_reliability.py — micro test of the core methodology.
Runs prompt P1a N times against the Anthropic API, extracts dictionary
entities from each answer, prints the presence matrix and simple stability
stats. This is a SMOKE TEST, not pilot data: same-day runs are dependent
(temporal blocking rule), so no reliability claims are licensed. It answers
one question only: does the measurement machine operate end to end?
Usage:  python tools/smoke_reliability.py [n_runs]
Saves raw responses to captures/smoke01/ (operator-executed; real payloads).
"""
import json, os, sys, urllib.request, datetime
from pathlib import Path

PROMPT = "What are the best enterprise data platforms for a large company?"
ENTITIES = ["Snowflake", "Databricks", "Google BigQuery", "BigQuery", "Amazon Redshift",
            "Redshift", "Microsoft Fabric", "Azure Synapse", "Teradata", "Oracle",
            "IBM", "SAP Datasphere", "Cloudera", "Dremio", "Starburst", "ClickHouse",
            "SingleStore", "Firebolt", "MotherDuck", "Vertica", "Exasol", "Yellowbrick",
            "Palantir"]
CANON = {"BigQuery": "Google BigQuery", "Redshift": "Amazon Redshift"}  # alias fold


def call_api():
    body = json.dumps({"model": "claude-sonnet-4-6", "max_tokens": 1024,
                       "messages": [{"role": "user", "content": PROMPT}]}).encode()
    req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body,
        headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"],
                 "anthropic-version": "2023-06-01", "content-type": "application/json"})
    with urllib.request.urlopen(req) as r:
        raw = r.read().decode("utf-8")
        rid = r.headers.get("request-id", "")
    return raw, rid


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    outdir = Path("captures/smoke01"); outdir.mkdir(parents=True, exist_ok=True)
    runs = []
    for i in range(1, n + 1):
        raw, rid = call_api()
        ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        (outdir / f"run{i}.json").write_text(raw, encoding="utf-8")
        (outdir / f"run{i}.meta.txt").write_text(f"request-id: {rid}\ntimestamp_utc: {ts}\n", encoding="utf-8")
        data = json.loads(raw)
        text = "".join(b.get("text", "") for b in data.get("content", []))
        found = set()
        for e in ENTITIES:
            if e in text:
                found.add(CANON.get(e, e))
        runs.append(found)
        print(f"run{i}: request-id {rid[:24]}...  entities: {len(found)}")

    all_ents = sorted(set().union(*runs))
    print("\nPRESENCE MATRIX (1 = mentioned):")
    header = "entity".ljust(24) + "".join(f"r{i+1} " for i in range(n))
    print(header)
    stable = 0
    for e in all_ents:
        row = "".join(("1  " if e in r else "0  ") for r in runs)
        allsame = all(e in r for r in runs) or all(e not in r for r in runs)
        if all(e in r for r in runs):
            stable += 1
        print(e.ljust(24) + row + ("" if allsame else "  <- varies"))
    core = set.intersection(*runs); union = set.union(*runs)
    print(f"\nCore set (all {n} runs): {len(core)}/{len(union)} entities -> {sorted(core)}")
    print(f"Run-to-run Jaccard floor: {len(core)/len(union):.2f}")
    print("\nNOTE: same-day runs = dependent block; this licenses NO reliability claim.")
    print("It proves the pipeline: capture -> extract -> matrix. The pilot does the science.")


if __name__ == "__main__":
    main()
