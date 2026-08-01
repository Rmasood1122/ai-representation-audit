# METHODOLOGY ARCHITECT — PASS 1 (GATES 0–5)
Input: whitepaper skeleton (constructs summary, panel spec, ICC thresholds, hash-chain, screen-fidelity fork).
Caveat: Gate 1 runs against the summary, not the full 1.1 document; re-run Gate 1 on 1.1 when complete.
Tags: [PROVEN] / [SUPPORTED] / [OPEN] / [VERIFY] per the Epistemic Contract. Confidence stated where judgment is mine.

---

## GATE 0 — MEASUREMENT-THEORETIC FOUNDATION

**What kind of quantity is "representation as a disposition"?**
[SUPPORTED] It is a **parameter of a conditional output distribution** — a behavioral propensity of a stochastic system given a query population. Formally analogous to a latent trait measured with error, but with a critical difference: the "error" (run-to-run variation) is partly a property of the *system under study*, not only of your instrument. Your framework must separate the two or a hostile expert will conflate them for you.

**Which measurement model?**
[SUPPORTED, confidence ~85%] **Generalizability Theory (G-theory), not raw ICC.** ICC(2,k) is a special case of a one-facet G-study; your design has at least five facets: prompt, paraphrase (nested in prompt), run, occasion/day, and capture surface (API/UI), with engine as a **fixed** facet (you do not generalize across engines — each engine gets its own coefficient). What G-theory changes:
- A **G-study** decomposes variance into components: between-entity (signal), between-prompt, between-run, between-day, residual. This answers the question ICC cannot: *where does instability live?* "Unstable across paraphrases but stable across runs" and the reverse are different findings with different products.
- A **D-study** then computes, from those components, how many prompts × runs × days you need to hit a target generalizability coefficient — replacing guesswork panel sizes with derived ones.
- Your ICC thresholds (0.80 / 0.60) transfer directly: apply them to the generalizability coefficient for your intended universe of generalization.
What would flip this: if pilot data shows variance components cannot be stably estimated at feasible n (check via CI width on components). [OPEN until pilot.]

**Critical ambiguity in your draft** [SUPPORTED]: "ICC with the prompt as the sampling unit" measures stability of *prompt-level* scores across runs. But your product scores *entities*. Reliability of what, generalized over what? If the reported index is entity-level, the object of measurement is the entity×engine×wave cell and prompts are a random facet you generalize over. Cross-examination question this closes: "Doctor, your reliability coefficient is computed on prompts, but your score is about companies. Explain." Fix in 1.1 before anything else.

**Scale properties** [SUPPORTED]: Mention/visibility rates are probabilities → ratio-scaled individually. Rankings are ordinal. Any *composite* index is at best interval-by-construction and must not support claims like "Brand A is twice as visible" unless built purely from rates. Publish the scale claim next to the index definition.

---

## GATE 1 — CONSTRUCT INTERROGATION (summary-level; re-run on full 1.1)

### C1: Entity representation / "a mention"
Attacks: negated mentions ("avoid X"), hedged mentions ("some users report..."), comparative mentions ("unlike X..."), mentions inside disclaimers, implicit reference without the name ("the market leader"), near-name collisions, rebrands/aliases, product-vs-parent-company, misspellings, multilingual surface forms, list-position effects.
**Rulebook stub** (decision rules a second coder can apply):
1. Frozen, hashed canonical-entity dictionary per vertical: entity → {aliases, products, prior names, common misspellings}. Additions logged, never retroactive within a wave.
2. A mention = any surface form resolving to a dictionary entry, **including negated and hedged forms**; polarity and hedging are coded as separate dimensions, never used to zero-out presence. (Otherwise "X is a scam" counts as invisibility — indefensible.)
3. Implicit references without a resolvable surface form: NOT a mention. Log frequency; if >5% of answers in a vertical, flag construct-coverage limitation.
4. Ambiguous collisions (Apple): context rule — count only if ≥1 disambiguating token from the dictionary's context set co-occurs; else code AMBIGUOUS, excluded from numerator and denominator, rate reported.
**Human-agreement requirement:** two independent coders, stratified sample ≥200 answer units per vertical, Krippendorff's α ≥ 0.80 on presence, ≥0.70 on polarity, before any automated scorer is trusted. [SUPPORTED — standard content-analysis practice; exact thresholds are convention, VERIFY against a content-analysis methods text.]
**Worst remaining ambiguity:** hedged-negative vs neutral polarity boundary. Accept as residual; report polarity with its own α.

### C2: Visibility
Attack: three incompatible operationalizations hide under one word — (a) presence probability, (b) prominence-weighted presence (position in answer/list), (c) share-of-voice vs competitors. Each moves differently and games differently. **Fix:** declare (a) presence probability as the primary endpoint; (b) and (c) as pre-registered secondary endpoints with separate reliability estimates. One construct per number.
**Gaming vector (A3), the serious one:** panel leakage. If the frozen panel becomes known, vendors optimize against your exact prompts and the index measures panel-targeting, not representation. **Fix:** publish only the panel's hash at pre-registration; maintain a rotating holdout sub-panel (~20%) never published even post-study; pre-commit that public-vs-holdout divergence beyond a threshold triggers a published gaming alert. This turns the gaming attempt into a detectable, publishable event. [NEW — not in draft.]

### C3: Screen-fidelity gap
Attacks: (i) pairing validity — paired captures separated in time confound surface difference with temporal drift; rule: pairs must complete within a fixed window (e.g., ≤10 min), window pre-registered, violations dropped and logged. (ii) The UI arm has its own account-state/geography/personalization variance; a clean-profile protocol (fresh session, logged-out where possible, fixed locale, documented) is part of the construct definition, not an operational detail. (iii) UI arm sample sizes will be far smaller than API — report the gap with CIs wide enough to be honest, never as a point estimate.

### C4: Representation reliability
Attack (the deepest one): low reliability is ambiguous between *your instrument failing* and *the system genuinely being unstable* — and only the second is your headline finding. Defense the design must support: (1) Gate 5 scorer validation caps instrument error from scoring; (2) G-theory decomposition attributes variance to named facets; (3) the daily canary bounds capture-pipeline drift. With those three, residual run/day variance is attributable to the system. Without them, RT-K1's "too unstable to score" is itself unsupported. [SUPPORTED]

---

## GATE 2 — SAMPLING DESIGN & POWER

**Power to distinguish ICC 0.80 from 0.60** [SUPPORTED, approximate]: CI width for reliability coefficients is driven mainly by the number of objects of measurement and facet levels. Analytic formulas exist for simple ICC designs [VERIFY: standard sources, e.g., Shrout & Fleiss tradition], but your crossed multi-facet design makes analytic power unreliable. **The defensible solo path is simulation:** run a cheap pilot (below), estimate variance components, then Monte-Carlo the full design under those components to find the smallest panel whose 95% CI separates 0.80 from 0.60. Pre-register the simulation code. This converts "is 15 prompts enough?" from hope into a computed answer. Confidence this is the right move: ~90%.

**Pilot (minimum defensible design):** 2 verticals × 10 prompts × 3 paraphrases × 5 runs spread over 5 days × 2 engines ≈ 3,000 calls. Cost: roughly $30–$300 depending on engines/lengths [SUPPORTED, order-of-magnitude]. Licenses only: variance-component estimates and the D-study. **It licenses no public claims about any brand.**

**Recommended design:** your full panel, with run counts set by the D-study, runs **blocked across days** (see Gate 3 — this is mandatory, not optional).

**Prompt-selection bias:** the panel's sampling frame must be named (which query-log source, what coverage, what's systematically missing — e.g., voice queries, logged-in personalized queries). The index generalizes only to that frame; publish the frame description with the panel hash. [SUPPORTED]

**Temporal confounds — tripwire and rule:** fingerprint (model string + system-fingerprint field where provided) logged per call; daily canary set scored for distribution shift. Pre-committed rule: any detected version change mid-wave splits the wave into sub-waves analyzed separately; pooling across versions requires an explicit, logged, pre-registered-exception decision. Silent pooling is the fraud vector A5 would use. [NEW: the *rule*; draft had only the canary.]

**Geographic/personalization variance (A4):** API arm: fix region per engine, document. UI arm: clean-profile protocol. Multi-region capture is a Stage-2 upgrade, not Stage-1 — record as residual risk, not scope creep.

---

## GATE 3 — STATISTICAL SPINE

**The exchangeability problem — your draft's biggest statistical hole** [SUPPORTED, confidence ~85%]: runs of the same prompt executed minutes apart may share caching, retrieval state, and A/B assignment. They are positively correlated for reasons that are not "the system's disposition." Consequence: reliability computed from time-adjacent runs is **inflated** — you would overstate stability, the exact error your credibility cannot survive (it's the vendors' error). **Corrections, in order of cost:**
1. **Temporal blocking (mandatory):** runs of a prompt spread across ≥3 distinct days. Cheap, closes most of the hole.
2. **Day as a random facet** in the G-study — quantifies it instead of assuming it away.
3. **Block bootstrap over days** for CIs, replacing the naive hierarchical bootstrap where day-clustering exists.
Cross-examination question closed: "Isn't your stability number just the cache being warm?"

**Estimator substitutions:**
- Fleiss' κ → **Krippendorff's α** for vendor disagreement: handles missing data (vendors cover different engines/prompts), any number of raters, and multiple measurement levels. κ's chance-agreement model is also a known attack surface. [SUPPORTED; VERIFY exact citation.] Tag: REVISED.
- Kendall's W for rank stability: KEEP, but only over entities with presence rate above a floor (ranking entities that appear in 2% of answers is noise laundering); floor pre-registered.
- Bayesian hierarchical reliability: offer **only as a pre-registered sensitivity analysis**, not the primary. Priors are an A1 attack surface; partial pooling benefits small cells but the primary must be the assumption-lighter frequentist G-coefficient. Tag: NEW (sensitivity only). This is a "no rigor theater" call: cut Bayesian-as-primary.

**Multiple comparisons:** ~5 verticals × 4 engines = 20 cells. Pre-commit: (1) primary endpoint = per-engine pooled reliability (4 numbers); (2) all 20 cells reported with CIs, descriptive; (3) any formal hypothesis tests across cells use Benjamini–Hochberg FDR at a pre-stated level. Decided now, before data. [NEW — absent from draft.]

**"What this number licenses" (publish-beside text, drafted):**
- *G-coefficient / ICC:* "This estimates how consistently this engine's answers would score this entity across the prompt panel and repeated occasions in this wave. It does not measure accuracy, fairness, or whether the representation is deserved, and it does not generalize beyond the panel's query frame or this model version."
- *Kendall's W:* "This measures whether the *ordering* of entities is stable across prompts/runs. High W with low presence rates means a stable ordering of rarely-mentioned entities — read both numbers together."
- *Krippendorff's α (vendor disagreement):* "This measures whether commercial tools agree with each other, not which one is correct. Low α means at most one of them can be right; it does not identify which."
- *Screen-fidelity loss rate:* "This estimates how often API-based measurement misses or adds entities relative to what a clean-profile user actually sees, per engine and vertical, within the paired-capture window. It is not a claim about any individual user's screen."

---

## GATE 4 — EVIDENCE-CHAIN FORENSICS

**The integrity/authenticity gap** [SUPPORTED]: your hash chain proves the archive hasn't changed since logging. It proves nothing about whether the payload *came from the engine*. A2's attack: "You could have generated these payloads locally and hashed them." Closures, ranked by threat-closed-per-dollar:
1. **Provider request IDs (near-free, highest value):** major APIs return per-request identifiers in response headers; log full headers verbatim. In litigation, the provider's own logs — reachable by subpoena — become the authenticity anchor your solo status can't provide. You don't need to prove authenticity alone; you need to preserve the hooks that let a court verify it. [SUPPORTED; header details per provider VERIFY.] Tag: NEW.
2. **External timestamp anchoring (near-free):** anchor daily chain digests via a trusted-timestamping service and/or public blockchain timestamping (e.g., OpenTimestamps-class [VERIFY]) in addition to monthly Zenodo. Closes backdating; multi-witness beats single-witness.
3. **Public digest witness (free):** daily digest pushed to a public git repo — independent third-party timestamp and visibility.
4. **UI arm:** screen-video of paired captures with NTP-synced clock overlay + session metadata. Heavier; reserve for litigation-track captures, not every panel run.
**What breaks under ToS (A4):** automated UI capture likely violates some engines' terms; API measurement may too if resold — per-engine counsel triage is correctly in your draft. Pre-commit the fallback: if an engine blocks or forbids, its cell reports "not measurable under access constraints" — a publishable finding, not a gap to paper over.
**Residual (cannot fully close solo):** fabrication-before-first-hash by the operator. Mitigations: request-ID hooks, external timestamps, standing replication invitation. State it in the limitations one-pager verbatim: "The operator could fabricate payloads before first hashing; request-ID preservation and third-party timestamps make this detectable under discovery, not impossible."

---

## GATE 5 — AUTOMATION VALIDITY (the scorer is an instrument)

[SUPPORTED throughout] The pipeline that turns raw answers into scores (entity resolution, presence, polarity, rank extraction) must be validated *as a measurement instrument* before any index built on it means anything:
1. **Gold standard:** stratified human-coded set, ≥300–500 answer units spanning all verticals/engines, dual-coded, disagreements adjudicated with logged rationales. Built once per wave-generation, versioned, hashed.
2. **Trust threshold:** automated scorer must reach agreement with gold ≥ the human–human α (and ≥0.80 on presence) per construct dimension. Below threshold → the dimension stays human-coded until fixed. Pre-registered.
3. **Drift monitoring:** fixed audit sample re-scored monthly; scorer version pinned and hashed like the panel; any scorer update forces re-validation against gold *before* deployment and a deviation-log entry. Score changes from scorer updates must never be attributable to the market.
4. **The circularity attack (A1):** "You used an LLM to judge LLMs — your judge shares the biases of the systems it judges." Defenses: deterministic rules wherever possible (dictionary-based resolution); where an LLM scorer is unavoidable (polarity, hedging), it is validated against *human* gold, its model family disclosed, and — where feasible — a different family from the engine being scored. Disclose regardless; this question WILL be asked.

---

## PASS 1 CUT LIST (rigor theater removed)
- Bayesian hierarchical model as primary estimator — priors are attack surface; demoted to sensitivity analysis.
- TLSNotary-style cryptographic session proofs — cost/complexity exceeds threat closed for a solo founder; request IDs + timestamps close most of the same gap. Residual logged.
- Multi-region capture at Stage 1 — real issue, wrong stage; logged as residual risk with a Stage-2 trigger.
- Per-entity reliability reporting at launch — n per entity too thin; report vertical- and engine-level reliability until D-study licenses finer grain.

## HANDOFF TO PASS 2
Gates 6–9 (integrity mechanisms, red-team simulation, external benchmarks/replication package, final spec + decision memo) run next, against this Pass 1 output. Flag for Gate 9's decision memo, provisionally: the single choice that most determines cross-examination survival is **the Gate 0 object-of-measurement fix** (entity-level vs prompt-level reliability) — everything else is repairable later; this one defines what every number means.
