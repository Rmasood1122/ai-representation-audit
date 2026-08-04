# AI Representation Audit

Pre-registered measurement program for brand and entity representation in AI answer engines.

**Pre-registration DOI (all versions):** https://doi.org/10.5281/zenodo.21782272
**This version (v1.0):** https://doi.org/10.5281/zenodo.21782273
**OSF project:** https://osf.io/d7k6g/overview

## Methodology
Generalizability Theory reliability estimation with forensic capture custody: SHA-256 hash chain, provider request-ID preservation, and a programmatic provenance gate (`gate/verify_provenance.py`).

**Pre-committed thresholds:** Phi >= 0.80 proceed · 0.60-0.80 caution with mandatory uncertainty disclosure · Phi < 0.60 triggers a published negative result (RT-K1).

## Repository map
- `docs/` — Document 1.1 (FROZEN 2026-08-01) and methodology audits
- `captures/` — verified paired captures with request-IDs (run01 = first gate exit 0)
- `gate/` — provenance ingestion gate
- `tools/` — manifest builder, probes, smoke tests
- `PREREGISTRATION_HASHES.txt` — SHA-256 manifest of the frozen state

## Integrity record
Deviation log entries DEV-001 and DEV-002 (see `docs/`) document fabrication incidents caught by this project's own custody design.
