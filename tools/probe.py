#!/usr/bin/env python3
"""probe.py — single-scenario capture probe for product testing.
Usage: python tools/probe.py LABEL "PROMPT" "Entity1,Entity2,..."
Saves raw payload + request-id to captures/probes/LABEL.json/.meta.txt
Prints: answer excerpt + which entities appeared. Operator-executed; real payloads.
"""
import json, os, sys, urllib.request, datetime
from pathlib import Path

label, prompt = sys.argv[1], sys.argv[2]
entities = [e.strip() for e in sys.argv[3].split(",")] if len(sys.argv) > 3 else []

body = json.dumps({"model": "claude-sonnet-4-6", "max_tokens": 1024,
                   "messages": [{"role": "user", "content": prompt}]}).encode()
req = urllib.request.Request("https://api.anthropic.com/v1/messages", data=body,
    headers={"x-api-key": os.environ["ANTHROPIC_API_KEY"],
             "anthropic-version": "2023-06-01", "content-type": "application/json"})
with urllib.request.urlopen(req) as r:
    raw = r.read().decode("utf-8"); rid = r.headers.get("request-id", "")

outdir = Path("captures/probes"); outdir.mkdir(parents=True, exist_ok=True)
(outdir / f"{label}.json").write_text(raw, encoding="utf-8")
ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
(outdir / f"{label}.meta.txt").write_text(f"prompt: {prompt}\nrequest-id: {rid}\ntimestamp_utc: {ts}\n", encoding="utf-8")

data = json.loads(raw)
text = "".join(b.get("text", "") for b in data.get("content", []))
print(f"=== {label} | request-id {rid[:28]}... ===")
print(text[:900] + ("..." if len(text) > 900 else ""))
if entities:
    hits = [e for e in entities if e in text]
    misses = [e for e in entities if e not in text]
    print(f"\nPRESENT: {hits}\nABSENT:  {misses}")
print(f"[saved captures/probes/{label}.json]")
