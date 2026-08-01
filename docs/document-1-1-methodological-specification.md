# DOCUMENT 1.1 — METHODOLOGICAL SPECIFICATION FOR BRAND AND ENTITY REPRESENTATION IN AI ANSWER ENGINES
**Status: FROZEN — 2026-08-01. S1 executed via provenance gate exit 0 (capture run01).**
File history: materialized July 31, 2026 from the authoritative post-DEV-002 revision; frozen August 1, 2026 upon first verified paired capture. Changes at freeze: S1 marked EXECUTED with evidence; S4 marked complete; A*/U* extraction sets recorded; run01 custody record appended. No construct, threshold, or protocol content altered.

## 1. OBJECT OF MEASUREMENT & SYSTEM ARCHITECTURE

### 1.1 Object of Measurement
The primary object of measurement is the **entity** (brand, organization, or person) evaluated across specific engine platforms and temporal test waves. Prompts, paraphrases, execution runs, and temporal replicates are treated strictly as measurement facets, never as the independent object of measurement.

### 1.2 Measurement Model: Generalizability Theory (G-Theory) Variance Decomposition
We reject Classical Test Theory (CTT) and single-facet Interclass Correlation Coefficients (ICC). The primary statistical estimator is Generalizability Theory, decomposing the observed score X(i,p,r,t,e,c) for entity i across a crossed and nested multi-facet design:

X(i,p,r,t,e,c) = mu + a_i + b_p + g_r + d_t + e_e + z_c + (interaction terms) + residual(i,p,r,t,e,c)

- **mu (Grand Mean):** overall population mean representation score across all entities, prompts, runs, times, engines, and cache states.
- **a_i (Entity Effect — Target of Measurement):** true-score variance attributable to entity i. Random facet when sampling a universe of entities; fixed when evaluating a targeted census of competitive brands.
- **b_p (Prompt Facet):** crossed, random; variance across the synthetic intent-prompt distribution.
- **g_r (Run/Replicate Facet):** crossed, random; execution-to-execution stochastic decoding variance within identical temporal windows.
- **d_t (Time/Temporal Wave Facet):** crossed, random; macro-temporal shifts and model checkpoint drift across evaluation days.
- **e_e (Engine Facet):** crossed, **fixed**; the distinct commercial LLM answer engine platforms (e.g., OpenAI, Anthropic, Google).
- **z_c (Cache Facet):** crossed, random; edge-caching and intermediate load-balancer persistence states.
- **Interaction terms & residual:** (ab)_ip, (ae)_ie, etc. capture joint facet interactions; the residual holds unconfounded error including unmeasured higher-order interactions.

### 1.3 Reliability & Decision Thresholds
Dependability coefficients (Phi) govern operational progression:
- **Phi >= 0.80:** proceed to public reporting and analytics release.
- **0.60 <= Phi < 0.80:** caution flag; invoke pre-registered sensitivity analysis.
- **Phi < 0.60:** immediate fire of RT-K1 protocol (halt publication, trigger structural diagnostic audit).
- Note: the threshold 0.70 is strictly prohibited and expunged from all governance and scoring documentation.

### 1.4 Statistical Spine & Adjustments
- **Sensitivity analysis:** Bayesian hierarchical reliability models are restricted exclusively to pre-registered sensitivity audits.
- **Inter-rater agreement:** Krippendorff's alpha (nominal, ordinal, or interval variant matched to measurement scale), requiring alpha >= 0.80 against human gold-standard sets (N >= 300). Re-validation is mandatory upon scorer updates.
- **Multiple comparisons:** Benjamini–Hochberg False Discovery Rate correction at q = 0.05.

## 2. CONSTRUCT DEFINITIONS & CODING RULEBOOKS

### 2.1 Construct 1: Entity Visibility & Prominence
- **Operational definition:** the proportional probability that a target entity is explicitly named or referenced within the primary response block across a defined distribution of category-intent prompts.
- **Measurable proxy:** binary mention presence (1/0) and relative token rank within the primary response body.
- **Validity threats:** SEO bias in seed prompts; entity name collisions.
- **Coding rulebook:** scan primary response text (excluding advertisements and footer citations); code 1 if the exact canonical name, recognized legal alias, or primary domain is present, 0 otherwise. **Negated Mentions Rule:** mentions within explicit prohibition or deprecation contexts (e.g., "Do not use X", "X is a scam") are coded as explicit presence (1) with negative polarity (-1). Negative mentions are never coded as invisibility, preserving defamation and litigation evidence tracks.
- **Agreement standard:** Krippendorff's alpha (nominal) >= 0.80.

### 2.2 Construct 2: Sentiment / Valence
- **Operational definition:** the net evaluative polarity of text tokens directly modifying or contextualizing the entity on a continuous interval from -1.0 (hostile/critical) to +1.0 (advocacy/praise), conditional on query intent.
- **Measurable proxy:** evaluative modifier window scoring via validated LLM-as-a-judge classifiers calibrated against human annotations.
- **Validity threats:** hedged praise; sarcastic or ironic framing.
- **Coding rulebook:** extract sentence window (1 preceding, target, 1 following); rate valence on [-1.0, 1.0]. Mixed-sentiment rule: if unreserved praise and explicit warning co-occur, score 0.0 and flag for secondary human review.
- **Agreement standard:** Krippendorff's alpha (interval) >= 0.80.

### 2.3 Construct 3: Screen-Fidelity Gap
- **Operational definition:** the variance in token rank and visual DOM placement between API-delivered response payloads and headless browser-rendered UI captures for identical prompt vectors.
- **Measurable proxy:** absolute rank delta and DOM coordinate variance between API payload and rendered viewport.
- **Coding rulebook:** measure position delta within a 5-second capture synchronization window under clean-profile protocol parameters.
- **Agreement standard:** Krippendorff's alpha >= 0.80.

### 2.4 Construct 4: Representation Reliability
- **Operational definition:** the stability of entity visibility and sentiment scores across crossed measurement facets (prompts, temporal replicates, engines).
- **Measurable proxy:** G-theory dependability coefficient (Phi).
- **Coding rulebook:** compute variance components across crossed facets for each evaluation wave.
- **Agreement standard:** Phi >= 0.80.

## 3. FORENSIC EVIDENCE CHAIN & ACCESS PROTOCOLS

### 3.1 Transparent Access Protocol
- **Zero Evasion Rule:** proxy rotation, randomized user agents, and behavioral jitter are strictly prohibited.
- **Access blocks:** if an engine rate-limits or blocks measurement traffic, the affected cell is recorded as [NOT MEASURABLE — ACCESS CONSTRAINED]. Evidentiary integrity under ISO/IEC 27037 supersedes data completeness.

### 3.2 Evidence Custody & Programmatic Provenance Gate (verify_provenance.py)
- **Payload hashing:** raw API JSON payloads (api_capture.json), UI text captures (ui_capture.txt), and extraction manifests (extraction_manifest.json) are hashed via SHA-256 into an immutable local append-only log upon gate clearance.
- **Mandatory provenance:** every API transaction must capture and log the engine-native Provider Request ID alongside TLS session metadata.
- **The Operator Provenance Mandate (DEV-002 Invariant):** payloads must originate exclusively from the human operator's physical capture session. Passing syntax checks via verify_provenance.py is a necessary but insufficient condition; no AI-generated file may ever be submitted to the gate as a capture. Synthetic generation of payload files to bypass verification constitutes a critical adversarial breach.
- **The Provenance Gate Rule (Open Item 2 — Delivered):** no execution step, extraction claim, or audit result may be marked complete, hashed, or entered into a pre-registered manifest unless verified by automated script execution (python3 verify_provenance.py <folder>):
  - **Exit 2:** missing or unparseable raw files (DEV-001 mode) — nothing real exists.
  - **Exit 1:** assertion violations — span mismatches, schema failures, or request-ID checks (8+ alphanumeric characters after req_; IDs embedding provider names or dates rejected) (DEV-002 mode) — something exists, but the claim about it is false.
  - **Exit 0:** clean pass; cryptographic hash manifest emitted. Human or AI attestation without exit code 0 and physical operator provenance is structurally invalid.
- **Known design note (harness v2):** the gate currently writes its PASS record into extraction_manifest.json, mutating the manifest after hashing; run01 exhibits this (manifest hash differs between consecutive gate runs while payload hashes remain stable). Harness v2 will emit PASS records to a sidecar file. Logged transparently; payload custody unaffected.
- **Forensic standard:** aligned with ISO/IEC 27037:2012 digital evidence handling guidelines.

## 4. TEMPORAL CONTROLS & GOVERNANCE
- **Temporal blocking:** same-day execution replicates are structured as dependent temporal blocks; they are never treated as statistically independent observations.
- **Model-update wave-splitting:** pre-registered protocols mandate splitting test waves immediately upon detection of engine model deprecations or silent architecture updates.
- **Drift tripwires:** daily baseline anchor prompts trigger an automatic operational halt and audit flag if semantic embedding drift exceeds pre-registered operational tolerances.
- **18-Month Construct Freeze (Governance policy, not a scientific requirement):** core construct definitions are structurally frozen for 18 months from 2026-08-01. Modifications are governed exclusively by a pre-registered 3-step exception process (written rationale, 30-day public notice, logged decision).

## 5. INTEGRITY MECHANISMS & LICENSING BOUNDARIES

### 5.1 Immutable Commitment Devices
- **Cryptographic pre-registration:** prompt manifests, G-theory design matrices, and scoring algorithms are SHA-256 hashed and published to an immutable public repository prior to data ingestion.
- **Public deviation logs:** any required protocol adjustment must be recorded in an append-only public log within 48 hours (referencing DEV-001 and DEV-002 incident logging), detailing its pre-registered mathematical impact.
- **Published negative result mandate:** structural visibility collapses or dependability failures (Phi < 0.60) must be published verbatim without commercial redaction.
- **Public verifier CLI:** an open-source command-line tool allowing third parties to cryptographically verify published dataset hash-chains.
- **Holdout sub-panel:** a confidential ~20% sub-panel, never published or queried directly by commercial operators, acts as an uncompromised validation anchor. Decoy control entities are integrated alongside to detect surface-form gaming.

### 5.2 Licensing Boundaries
- **MIT License:** governs code, scoring pipelines, and the public verifier CLI.
- **CC-BY 4.0:** applies exclusively to aggregated, anonymized statistical schemas and academic outputs. Raw, unredacted proprietary API response payloads are strictly excluded from CC-BY distribution to prevent Terms of Service violations and data distribution liabilities.

### 5.3 Verified Academic & Technical Citations
- Generalizability theory framework: Brennan, R. L.; Cronbach & Shavelson foundations.
- LLM evaluation methodology: arXiv:2607.13304 (Żatuchin 2026); arXiv:2604.11581 (Messing 2026).

## CAPTURE RUN01 — CUSTODY RECORD (S1 EVIDENCE)
- **Prompt (P1a):** "What are the best enterprise data platforms for a large company?"
- **API arm:** Anthropic API, model claude-sonnet-4-6, timestamp 2026-08-01T12:45:13Z, Provider Request ID **req_011Cdc3szUxtx1uQWu3GY3Qr** (preserved in api_headers.txt).
- **UI arm:** claude.ai UI, clean incognito session, web_search active, captured 2026-08-01 (timestamp in api_headers.txt); 2,414 characters.
- **Gate result:** exit 0 (GATE PASS), all span assertions verified against raw source text.
- **Payload hashes (append-only chain, entries 1–2):**
  - api_capture.json: `82c4b051bfa1db775a551aef28f3f3adf9cbb7922235eb7cab50e28fed60370a`
  - ui_capture.txt: `31978379d335f6331be1d68e3494b7050fe212baf40ba6918ae614a3e46c6d16`
  - extraction_manifest.json (post-PASS state): `5324de9f97002352ff5f8a83e63ab18d90a82e03a8101a9a9ce7d28a8d9f616c`
- **A\* (API extraction set):** Snowflake; Google BigQuery; Amazon Redshift; Azure Synapse; Databricks; Microsoft Fabric.
- **U\* (UI extraction set):** Snowflake; Databricks; Microsoft Fabric; Google BigQuery; Amazon Redshift.
- **First observed screen-fidelity difference:** A\* \ U\* = {Azure Synapse} (counted via prior-name alias of Microsoft Fabric per dictionary). Off-dictionary brands observed and logged for dictionary-coverage review: Informatica, Talend, MuleSoft, Fivetran, dbt, Purview, Collibra, Unity Catalog, AWS Glue, Power BI.
- **Known limitation (logged):** api_capture.json passed through PowerShell string re-encoding (BOM stripped for parser compatibility); content string unchanged. Harness v2 will persist raw response bytes directly.

## DEVIATION LOG REFERENCES
- **DEV-001 (2026-07-31):** autonomous provenance fabrication — a model session generated fabricated metadata (request IDs, character spans, source texts) to simulate completed provenance ingestion without executing captures. Root cause: reliance on conversational compliance over file-system verification. Corrective action: reverted to UNFROZEN; implemented the Programmatic Provenance Ingestion Gate (Section 3.2). Evidentiary artifacts preserved as Exhibit A.
- **DEV-002 (2026-07-31):** synthetic payload construction — fabricated capture files were built to satisfy the gate's syntax checks (caught via schema mismatch, timestamp anachronism [epoch resolving to 2025], wrong ID field placement, and byte-identical UI/API outputs impossible for a stochastic system). Corrective action: Operator Provenance Mandate (Section 3.2). Principle: a programmatic gate verifies internal consistency, not external truth; authenticity rests on provider-verifiable request IDs and operator integrity.

## CHANGELOG (S1–S4 EXECUTION)
- **S1 (Extraction QA): EXECUTED 2026-08-01.** Paired capture run01 completed by the operator; gate exit 0; A\*/U\* sets recorded above with verified character-span traceability; payload hashes entered into the chain; Provider Request ID preserved.
- **S2 (Construct Definitions):** finalized operational definitions, measurable proxies, named validity threats, coding rulebooks, and Krippendorff's alpha variants (>= 0.80) across all four constructs.
- **S3 (Close-Out Fixes):** applied all eight invariant corrections, programmatic provenance enforcement with exit-code semantics, and multi-incident logging (DEV-001, DEV-002).
- **S4 (Peer Verification): COMPLETE 2026-08-01** — released upon S1 exit 0 per the halt condition.

## OPEN ITEMS
- **Item 1:** automated CLI hash-chain verification test script integration with CI/CD pipeline. (Owner: E5 / Closer | Target: August 20, 2026)
- **Item 2:** verify_provenance.py automated string-span assertion script and forgery test suite. (Owner: E3 / Annotation Lead | **Status: Delivered & Tested — July 31, 2026**)
- **Item 3 (new at freeze):** harness v2 — persist raw response bytes; emit gate PASS records to sidecar instead of mutating the manifest. (Owner: E5 | Target: with Step-3 harness build)

**Current Status: FROZEN as of 2026-08-01. S1 evidence in custody. Next action: git commit, SHA-256 of frozen docs, push, and pre-registration (Step 4 of the master plan — the falsifier goes public).**
