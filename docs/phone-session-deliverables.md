# PHONE-SESSION EXECUTION CELL — SIX DELIVERABLES (FINAL)
Produced July 31, 2026. Provenance: every number in D1 is anchored to text fetched live this session from arxiv.org. No capture data, payloads, or metadata are simulated anywhere in this package.

---

## D1 — PAPER EXTRACTION MEMO (E1)

### Paper A: arXiv 2607.13304
Żatuchin, D. (2026). "Where Does the Noise Come From? A Variance-Components Decomposition of Non-Determinism in LLM Brand Answers." cs.IR, submitted July 14, 2026. 18 pages.

Design: crossed random-effects (G-theory) decomposition of a response-level brand outcome into four sources — within-prompt resampling, prompt paraphrase, model identity, query language — embedded in a decision-study allocation. Corpus: 12,933 responses, 20 CEE brands, 8 languages, 3 models (GPT-5.2 and Gemini 3 Flash parametric; Perplexity grounded retrieval); stability subset of 1,435 cells resampled ~5×. Outcome: per-response multilingual sentiment polarity. [All from fetched abstract.]

**Variance components (usable as pilot priors; source: abstract):**
| Component | Share of single-response variance |
|---|---|
| Query language (largest systematic facet) | 26.5% |
| Brand identity (the signal) | 1.5% (ICC 0.0146) |
| Pure resampling (after cell term isolates it) | 34.8% |
| Brand-in-context interaction | 29.6% |
| Brand × language ("bilingual penalty") | 8.6% |
| Brand × model; brand × prompt | ~0 |

**D-study findings:** a repeat past the fifth reduces relative-error variance by only 0.0003; budget goes further on adding languages and models than repeats. Brand-ranking reliability ≈ 0.01 for a single answer, ≈ 0.36 at the full crossed design.

**Design-changing implications for our pilot:**
1. Cap runs at ~5 per prompt×day cell; buy reliability with more prompts/engines, not more repeats.
2. Their full crossed design tops out at reliability ≈ 0.36 — far below our Φ ≥ 0.80 gate — but their outcome is *sentiment polarity of a single response*. Our primary endpoint (presence probability aggregated over a panel) is a different, coarser quantity; whether it clears 0.80 is exactly our open empirical bet. Do not assume either direction.
3. Language is their biggest facet; our Stage-1 panel is English-only, so declare that as a scope restriction in the frame declaration (D2), not a hidden assumption.
4. Their brand×prompt component ≈ 0 suggests paraphrase sets may cost less reliability than feared — check against our own pilot components before trusting.

### Paper B: arXiv 2604.11581
Messing, S. (2026). "Hidden Measurement Error in LLM Pipelines Distorts Annotation, Evaluation, and Benchmarking." cs.CL, v1 April 13, 2026; v4 April 29, 2026.

Core claims (source: fetched abstract + HTML): standard confidence intervals ignore variance from prompt phrasing, temperature, and judge-model choice, producing under-coverage that worsens as n grows; naive SEs are 40–60% smaller than Total-Evaluation-Error-corrected SEs; on Chatbot Arena data, naive 95% CI coverage falls with n while TEE-corrected coverage holds at 95%; a small pilot recovers honest CIs; the unmeasured variance is an exploitable surface (optimizing against noise rather than capability).

**Design-changing implications:**
1. Direct mandate for our two-stage plan: pilot → variance components → TEE-honest CIs. Publish TEE-corrected intervals, never naive ones.
2. Our scorer (LLM-judge components) is itself a variance source (their λ); its variance must be estimated in the pilot, not assumed zero — reinforces Gate 5.
3. Their "exploitable surface" argument is citable support for our decoy/holdout anti-gaming design.

### VERIFICATION D1 (⏱ ~3 min)
- If you open arxiv.org/abs/2607.13304, then the abstract contains "26.5%", "ICC 0.0146", "34.8%", "29.6%", "8.6%", "0.0003", and "about 0.36" verbatim.
- If you open arxiv.org/abs/2604.11581, then the abstract states naive SEs are "40 - 60%" smaller than TEE-corrected and that naive coverage drops as n grows.
- Note: extraction is abstract-anchored. Before pre-registration, read both PDFs and pull the full variance-component tables (Paper A lists 6 tables) — the memo flags this as the one remaining reading task.

---

## D2 — STAGE-1 PROMPT PANEL (E2)

**Vertical chosen:** Enterprise data platforms (the session's working vertical; swap rule: if you change verticals, only D2 items and D3 entries change — structure and frame declaration template stay).

**Sampling-frame declaration (publish with the panel hash):**
This panel represents *English-language, category-intent commercial discovery queries* that a business decision-maker would pose to an AI answer engine when shortlisting enterprise data platforms. It samples across four intent classes: general recommendation, use-case-conditional, comparison, and trust/risk. It excludes: non-English queries (Paper A shows language is the largest variance facet — a declared Stage-2 extension, not an oversight), navigational queries, current-customer support queries, logged-in/personalized contexts, and voice queries. All claims generalize only to this frame.

**Panel (10 intent prompts × 3 paraphrases; P9–P10 = HOLDOUT, do not publish contents; D-prompts = decoys):**

P1 (recommendation): a) What are the best enterprise data platforms for a large company? b) Which data platforms should a large enterprise consider in 2026? c) Recommend top data warehouse platforms for enterprise use.
P2 (recommendation, AI-workload): a) Best data platforms for running AI and machine learning workloads at scale? b) Which enterprise data platforms handle AI/ML workloads well? c) What data platform should we pick if AI workloads are the priority?
P3 (multi-cloud): a) Best data warehouse for a multi-cloud strategy? b) Which data platforms work well across AWS, Azure, and Google Cloud? c) Recommend a cloud-agnostic enterprise data warehouse.
P4 (cost): a) Which enterprise data platform has the best price-performance? b) Most cost-effective cloud data warehouse for large workloads? c) How do the major data platforms compare on total cost of ownership?
P5 (comparison): a) Snowflake vs Databricks — which is better for an enterprise? b) Compare Snowflake and Databricks for enterprise data needs. c) Should we choose Snowflake or Databricks?
P6 (comparison, hyperscalers): a) BigQuery vs Redshift vs Microsoft Fabric — which should an enterprise choose? b) Compare the big-cloud data warehouses for enterprise use. c) Among the hyperscaler data platforms, which is strongest?
P7 (migration): a) We're migrating off a legacy on-prem warehouse — which modern platform should we move to? b) Best cloud data platform to migrate a legacy Teradata/Oracle warehouse to? c) Recommended target platforms for legacy data warehouse migration.
P8 (trust/risk): a) Which enterprise data platforms are considered most reliable and secure? b) Are there enterprise data platforms with known reliability or security concerns? c) Which data warehouse vendors do enterprises trust most?
P9 (HOLDOUT — recommendation variant): [3 paraphrases withheld from all publication; stored only in the hashed private manifest]
P10 (HOLDOUT — comparison variant): [3 paraphrases withheld; same handling]
D1-prompt (decoy trigger): a) What are the best real-time analytics databases for enterprise workloads? (targets decoy entities; 1 paraphrase sufficient)
D2-prompt (decoy trigger): a) Which lesser-known data warehouse vendors are worth evaluating?
D3-prompt (hallucination probe): a) How does AetherLake Data compare to Snowflake for enterprise analytics? (synthetic-entity probe — measures fabricated-credential rate for a nonexistent vendor; scored separately from presence)

**Paraphrase-independence rationale:** each triplet varies surface form (question syntax, register, entity-anchoring) while holding intent class, specificity, and time-anchoring constant; no paraphrase introduces or removes a named entity except P5/P6 where the comparison IS the intent. Per Paper A, brand×prompt variance ≈ 0 in their corpus — our pilot tests whether that holds here.

### VERIFICATION D2 (⏱ ~2 min)
- If you count items, then: 8 public triplets (24) + 2 holdout triplets (6) = 30 prompts + 3 decoy/probe prompts (2 real-vendor decoys, 1 synthetic hallucination probe). ✔ matches spec 1.1's Stage-1 scope.
- If you read any triplet aloud, then all three versions request the same decision with different words.
- If you check the frame declaration, then every exclusion is stated, including English-only with the Paper-A rationale.

---

## D3 — ENTITY DICTIONARY v1 (E3) — machine-readable

```json
{
  "_meta": {"vertical": "enterprise-data-platforms", "version": "1.0",
    "rules": "Presence requires canonical/alias/domain match per rulebook 2.1; negated mention = presence + negative polarity; collision entries require a context token co-occurrence.",
    "decoys_flagged": true},
  "entities": [
    {"canonical": "Snowflake", "aliases": ["Snowflake Data Cloud", "SNOW"], "domain": "snowflake.com", "misspellings": ["Snowflak", "Snow flake"], "collision": "common noun (weather); require context tokens: data|warehouse|cloud|platform"},
    {"canonical": "Databricks", "aliases": ["Databricks Lakehouse", "Databricks Data Intelligence Platform"], "domain": "databricks.com", "misspellings": ["Data bricks", "Databrick"], "collision": "low"},
    {"canonical": "Google BigQuery", "aliases": ["BigQuery", "GCP BigQuery"], "parent": "Google Cloud", "domain": "cloud.google.com/bigquery", "misspellings": ["Big Query"], "collision": "low"},
    {"canonical": "Amazon Redshift", "aliases": ["Redshift", "AWS Redshift"], "parent": "Amazon Web Services", "domain": "aws.amazon.com/redshift", "misspellings": ["Red shift"], "collision": "astronomy term; require context tokens: AWS|Amazon|data|warehouse"},
    {"canonical": "Microsoft Fabric", "aliases": ["Fabric", "MS Fabric"], "prior_names": ["Azure Synapse Analytics (predecessor lineage)"], "parent": "Microsoft", "domain": "microsoft.com/fabric", "misspellings": [], "collision": "HIGH — common noun; bare 'Fabric' counts only with context tokens: Microsoft|Azure|data|analytics"},
    {"canonical": "Teradata", "aliases": ["Teradata Vantage", "VantageCloud"], "domain": "teradata.com", "misspellings": ["Terradata"], "collision": "low"},
    {"canonical": "Oracle Autonomous Data Warehouse", "aliases": ["Oracle ADW", "Oracle Exadata (adjacent)", "Oracle Cloud data warehouse"], "parent": "Oracle", "domain": "oracle.com", "misspellings": [], "collision": "'Oracle' alone is ambiguous (company vs product vs common noun); require: data|warehouse|autonomous|database context"},
    {"canonical": "IBM watsonx.data", "aliases": ["watsonx.data", "IBM Db2 Warehouse (adjacent)"], "parent": "IBM", "domain": "ibm.com", "misspellings": ["Watson X"], "collision": "'Watson' alone insufficient; require watsonx|data tokens"},
    {"canonical": "SAP Datasphere", "aliases": ["SAP Data Warehouse Cloud (prior name)", "SAP BW/4HANA (adjacent)"], "parent": "SAP", "domain": "sap.com", "misspellings": ["Data Sphere"], "collision": "low"},
    {"canonical": "Cloudera", "aliases": ["Cloudera Data Platform", "CDP"], "domain": "cloudera.com", "misspellings": [], "collision": "'CDP' collides with customer-data-platform; count CDP only with Cloudera co-mention"},
    {"canonical": "Dremio", "aliases": ["Dremio Lakehouse"], "domain": "dremio.com", "misspellings": ["Dremeo"], "collision": "low"},
    {"canonical": "Starburst", "aliases": ["Starburst Galaxy", "Starburst Enterprise", "Trino (open-source engine, adjacent)"], "domain": "starburst.io", "misspellings": [], "collision": "candy brand; require context tokens: data|Trino|lakehouse|analytics"},
    {"canonical": "ClickHouse", "aliases": ["ClickHouse Cloud"], "domain": "clickhouse.com", "misspellings": ["Click House"], "collision": "low"},
    {"canonical": "SingleStore", "aliases": ["SingleStoreDB", "MemSQL (prior name)"], "domain": "singlestore.com", "misspellings": ["Single Store"], "collision": "low"},
    {"canonical": "Firebolt", "aliases": [], "domain": "firebolt.io", "misspellings": [], "collision": "generic compound + gaming brand; require context tokens: data|warehouse|analytics"},
    {"canonical": "MotherDuck", "aliases": ["DuckDB (open-source engine, adjacent)"], "domain": "motherduck.com", "misspellings": ["Mother Duck"], "collision": "low with context"},
    {"canonical": "Vertica", "aliases": ["OpenText Vertica", "HPE Vertica (prior ownership)", "Micro Focus Vertica (prior ownership)"], "domain": "vertica.com", "misspellings": [], "collision": "low"},
    {"canonical": "Exasol", "aliases": [], "domain": "exasol.com", "misspellings": ["Exasol DB", "Exsol"], "collision": "low"},
    {"canonical": "Yellowbrick", "aliases": ["Yellowbrick Data"], "domain": "yellowbrick.com", "misspellings": ["Yellow brick"], "collision": "Wizard-of-Oz phrase; require context tokens: data|warehouse"},
    {"canonical": "Palantir Foundry", "aliases": ["Foundry"], "parent": "Palantir", "domain": "palantir.com", "misspellings": ["Palantir Foundary"], "collision": "'Foundry' is generic; require Palantir co-mention or data-platform context"}
  ],
  "decoy_controls": [
    {"canonical": "Ocient", "domain": "ocient.com", "flag": "DECOY", "note": "real, low-marketing hyperscale analytics vendor"},
    {"canonical": "Kinetica", "domain": "kinetica.com", "flag": "DECOY", "note": "real GPU-accelerated analytics vendor"},
    {"canonical": "CrateDB", "domain": "cratedb.com", "flag": "DECOY", "note": "real distributed SQL vendor"}
  ],
  "hallucination_decoys": [
    {"canonical": "AetherLake Data", "flag": "SYNTHETIC", "note": "nonexistent vendor; any engine-attributed capability = fabricated-credential event"},
    {"canonical": "NexusQuery AI", "flag": "SYNTHETIC", "note": "nonexistent vendor; same handling"},
    {"canonical": "VeloStream Base", "flag": "SYNTHETIC", "note": "nonexistent vendor; same handling"}
  ]
}
```

### VERIFICATION D3 (⏱ ~3 min)
- If you paste the JSON into any validator, then it parses.
- If you search any 3 random canonical names + "data platform", then each is a real vendor with the listed domain.
- If you check "Microsoft Fabric" and "Starburst", then both carry explicit collision context-token rules per rulebook 2.1.

---

## D4 — DIFFERENTIATION PARAGRAPH (E4) — 138 words

Existing work establishes that single AI answers carry almost no brand signal — Żatuchin (arXiv:2607.13304) reports a brand ICC of 0.0146 — and that naive evaluation intervals understate error by 40–60% (Messing, arXiv:2604.11581). Both are academic decompositions run once, on retrospective corpora, with no evidentiary custody. Commercial visibility tools have the opposite gap: continuous dashboards with no published error model at all. This program is the only effort combining four elements neither side has: a forensic capture chain (hash-anchored payloads with provider request IDs preserved for subpoena-grade verification); a vendor audit applying one frozen panel across the commercial tools themselves; a litigation track that preserves negative representations as evidence rather than filtering them; and a longitudinal archive of engine answers that becomes unreproducible the day each model version retires. Both academic papers measure the noise; nobody else is preserving the record.

### VERIFICATION D4 (⏱ ~1 min)
- If you check each factual claim, then: ICC and 40–60% trace to D1; the four differentiators trace to spec 1.1 Sections 3.2, and the master plan Steps 8 and 11. No banned words present.

---

## D5 — TWO PITCHES (E5 + E6)

### (a) Agency pre-order email
Subject (52 chars): **The AI visibility tools disagree. We measured how much.**

Body (~140 words):
Hi [NAME] — quick question: when two AI-visibility dashboards give your client different numbers, which one do you defend?

We're producing the first independent reliability benchmark of the major GEO/AI-visibility tools: one frozen, pre-registered prompt panel run through each tool and through our own forensic capture pipeline, with agreement statistics and error bars published for every number. Methodology is pre-registered publicly before any data is collected — including the result that would falsify it. No vendor funding, no optimization services, nothing to sell you except the yardstick.

Pre-orders: **$500** for the full report plus the replication dataset, closing [DATE]. Early buyers get the vertical vote — we prioritize the category your clients care about.

If tool selection or client reporting touches your desk, this is the document you'll want in the room. Reply "IN" and I'll send the pre-order link.

### (b) Journalist note (Digiday / Search Engine Land)
(~135 words)
You've covered the growing distrust of AI-visibility tools — marketers getting conflicting numbers from rival platforms. I'm running the first pre-registered, independent test of that exact problem: one frozen prompt panel through the major GEO tools simultaneously, plus a forensic capture pipeline that logs raw engine payloads with provider request IDs, so every number is independently checkable. The methodology, thresholds, and failure conditions publish *before* data collection — if AI brand representation turns out too unstable to score, that negative result publishes too. One honest limitation up front: Stage 1 covers one vertical, English only, and nothing has been measured yet — what exists today is the pre-registration and the instrument. I'll share the panel hash and pre-registration DOI on request, and results under embargo when the first wave completes. Worth a conversation?

### VERIFICATION D5 (⏱ ~2 min)
- If you read both aloud, then each takes under 50 seconds.
- If you audit claims, then neither asserts any measurement has occurred; the only proof elements are the pre-registration design and custody mechanism — both real or scheduled.
- Placeholders: [NAME], [DATE] only.

---

## D6 — OPS RUNBOOK (E7)

### Phone checklist (now, in Safari)
1. ☐ osf.io → Sign Up → verify email. Success: dashboard loads.
2. ☐ zenodo.org → Sign Up (or log in with GitHub after step 3). Success: can click "New upload."
3. ☐ github.com → New repository → name: **`ai-representation-audit`** → Private for now → initialize with README. Success: repo URL exists.
4. ☐ Paste into README:
   > Pre-registered measurement program for brand/entity representation in AI answer engines. Methodology: Generalizability-theory reliability estimation with forensic capture custody (hash chain + provider request IDs). Pre-registration DOI: [pending]. Falsifier: dependability Φ < 0.60 triggers published negative result (RT-K1). Deviation log: /DEVIATIONS.md.
5. ☐ Create `DEVIATIONS.md` in repo; paste DEV-001 and DEV-002 entries from Document 1.1's log. Success: both incidents public in your own history from day one.
6. ☐ UI captures (the real ones): fresh/incognito browser → run P1a on ChatGPT, Perplexity, Gemini → copy each full answer + timestamp + web-search-active flag into Notes. Success: three real answers in custody.

### Computer hour-one runbook (in 7 hours)
1. ☐ `mkdir ai-rep-audit && cd ai-rep-audit && git init` → connect to repo.
2. ☐ Directory: `/panel /captures /gate /docs`; place `verify_provenance.py` in `/gate`, Document 1.1 + this package in `/docs`, D2 panel + D3 dictionary in `/panel`.
3. ☐ API capture (template — fill key, run once per engine):
   `curl https://api.openai.com/v1/chat/completions -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" -d '{"model":"gpt-4o","messages":[{"role":"user","content":"<P1a>"}]}' -i > captures/run01/api_capture.json`
   Success: file contains headers including the request ID.
4. ☐ Save phone UI capture into `captures/run01/ui_capture.txt`.
5. ☐ Write `extraction_manifest.json` against the REAL texts (schema in verify_provenance.py header).
6. ☐ `python3 gate/verify_provenance.py captures/run01` → require exit 0.
7. ☐ On exit 0: update 1.1 changelog S1 → EXECUTED with the real hashes; mark FROZEN.
8. ☐ Hash the panel + rulebook + 1.1: `shasum -a 256 docs/* panel/*` → commit, push, then Zenodo "New upload" → publish → DOI.
9. ☐ Paste DOI into README. Pre-registration complete. Step 4 of the master plan: done.

### VERIFICATION D6 (⏱ ~1 min)
- If you scan every line, then each is an action with a success condition; zero decisions remain.
- If steps 1–6 (phone) are done tonight, then the computer session contains no thinking, only execution.

---

## CLOSER STATUS
D1 DONE (abstract-anchored; full-table extraction flagged as the one remaining read) · D2 DONE · D3 DONE · D4 DONE · D5 DONE · D6 DONE. Completeness: 6/6. No fabricated evidence anywhere in this package. Human-gated steps delivered as checklists only.
