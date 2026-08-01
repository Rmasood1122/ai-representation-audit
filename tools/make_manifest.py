#!/usr/bin/env python3
"""make_manifest.py — builds extraction_manifest.json from REAL capture files.
Reads files exactly as verify_provenance.py does, so spans always match the gate.
Usage: python make_manifest.py <capture_dir>
"""
import json, sys, re
from pathlib import Path

UI_SURFACES = ["Snowflake", "Databricks", "Microsoft Fabric", "Google BigQuery", "Amazon Redshift"]
API_SURFACES = ["Snowflake", "Google BigQuery", "Amazon Redshift", "Azure Synapse", "Databricks", "Microsoft Fabric"]
API_JSON_PATH = ["content", 0, "text"]  # Anthropic Messages shape


def spans_for(text, surfaces, label):
    out = []
    for s in surfaces:
        i = text.find(s)
        if i == -1:
            print(f"  [{label}] NOT FOUND: {s} (skipped)")
            continue
        out.append({"surface": s, "start": i, "end": i + len(s)})
        print(f"  [{label}] {s} -> [{i},{i+len(s)})  source_check='{text[i:i+len(s)]}'")
    return out


def main():
    d = Path(sys.argv[1])
    api_raw = json.loads((d / "api_capture.json").read_text(encoding="utf-8"))
    ui_text = (d / "ui_capture.txt").read_text(encoding="utf-8")
    node = api_raw
    for k in API_JSON_PATH:
        node = node[k] if isinstance(k, str) else node[int(k)]
    api_text = node

    headers = (d / "api_headers.txt").read_text(encoding="utf-8", errors="replace")
    rid = re.search(r"request-id:\s*(\S+)", headers)
    ts_api = re.search(r"^timestamp_utc:\s*(\S+)", headers, re.M)
    ts_ui = re.search(r"ui_timestamp_utc:\s*(\S+)", headers)
    ws = "yes" in (re.search(r"web_search:\s*(\S+)", headers).group(1).lower() if re.search(r"web_search:\s*(\S+)", headers) else "")

    print("Cutting spans against real file text:")
    manifest = {
        "prompt": "What are the best enterprise data platforms for a large company?",
        "api": {
            "engine": "Anthropic API",
            "model": api_raw.get("model", ""),
            "timestamp_utc": ts_api.group(1) if ts_api else "",
            "request_id": rid.group(1) if rid else "",
            "answer_json_path": API_JSON_PATH,
            "entities": spans_for(api_text, API_SURFACES, "A*"),
        },
        "ui": {
            "engine": "claude.ai UI",
            "timestamp_utc": ts_ui.group(1) if ts_ui else "",
            "locale": "en-US",
            "web_search_active": ws,
            "entities": spans_for(ui_text, UI_SURFACES, "U*"),
        },
        "notes": "Azure Synapse counted via prior-name alias of Microsoft Fabric per dictionary. Off-dictionary brands observed and logged separately (Informatica, Talend, MuleSoft, Fivetran, dbt, Purview, Collibra, Unity Catalog, AWS Glue, Power BI).",
    }
    (d / "extraction_manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {d/'extraction_manifest.json'} — now run the gate.")


if __name__ == "__main__":
    main()
