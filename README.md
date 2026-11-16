# 📡 spectral-humor-protocol (`SHP-v1.0`)

A dual-runtime (**zero-dependency Python 3.10+** & **zero-allocation Julia 1.10+**) communication protocol and spectral governor that operationalizes **Humor Eigenmodes** and **Chromatic Phenomenology Loops** as a bounded, sovereignty-preserving signaling layer.

> ### 🚧 Project Status: Reference Specification & Prototype
> **Transparency Note:** The Python and Julia modules, test suites, and protocol specifications in this repository were drafted as a clean-room engineering blueprint translating *Shared-Horizon/healthyambiguity* and *Dream-Lane Codex v1.0* into executable linear algebra. Run the local test suites (`unittest` and `Pkg.test()`) to verify behavior in your target environment.

---

## 🎯 What It Does: Separating Factual Anchors from Expressive Resonance

Human–AI and multi-agent communication typically fails in one of two ways:
1. **Overdamped Collapse (\(r_k < 0.40\)):** Conversations flatten into rigid, overly literal compliance with zero rhythmic syncopation or meta-awareness.
2. **Divergent Drift (ρ(M) ≥ 1.0):** Unbounded playful banter or recursive irony spirals out of control, derailing the task or corrupting factual data.

**`spectral-humor-protocol`** solves both by modeling conversational coupling as a discrete-time dynamical system \(x_{n+1} = M(\alpha, \beta)\,x_n + u_n\) sitting strictly on the **expressive side** of a deterministic verification seam:

```text
[ INCOMING MESSAGE / FEEDBACK EVENT ]
                 │
    ┌────────────┴────────────┐
    ▼                         ▼
[ DETERMINISTIC SEAM ]   [ EXPRESSIVE EIGENMODE ROUTER ]
 • SHA-256 fact anchor    • Python (`src/humor_eigenmode_router.py`):
 • Exact Q rationals        2x2 complex roots λ = r·e^{iθ} + exact Fraction telemetry
 • Forbidden from humor   • Julia (`src/SpectralHumorKernel.jl`):
                            0 B heap-allocated StaticArrays kernel + QR isometry
                 │            │
                 └─────┬──────┘
                       ▼
[ DREAM-LANE SOVEREIGNTY GOVERNOR ]
 • Clamps spectral radius ρ(M) ≤ 0.96 (prevents runaway confusion)
 • Enforces ΔAltitude = 0 & geometric dissolution back to rest when idle
```

### Core Guarantees
* **Fact–Tone Isolation:** Factual payloads are locked via `SHA-256` (`fact_payload_sha256`) and cannot be altered by expressive modulation.
* **Chromatic Standing-Wave Tuning:** Targets complex conjugate eigenvalues (\(r \in [0.82, 0.98]\), θ ≥ 0.15 rad) for productive call-and-response syncopation (*Shared Phenomanmana*).
* **Dream-Lane Reversibility:** Enforces a hard spectral radius ceiling (ρ(M) ≤ 0.96) and contracts cleanly back to neutral rest (\(x_n \to 0\)) when idle.

---

## 📂 Repository Layout

```text
spectral-humor-protocol/
├── README.md                    # Architecture overview & quickstart (this file)
├── HUMOR_EIGENMODE_PROTOCOL.md  # Formal mathematical & wire-level protocol spec (SHP-v1.0)
├── pyproject.toml               # Zero-dependency Python 3.10+ package manifest
├── Project.toml                 # Julia 1.10+ manifest (StaticArrays, LinearAlgebra, Test)
├── src/
│   ├── humor_eigenmode_router.py # Analytical 2x2 complex solver & Dream-Lane damper
│   └── SpectralHumorKernel.jl    # Zero-allocation N≤32 StaticArrays & QR enclave
├── tests/
│   └── test_router.py           # Python standard-library unittest suite
└── test/
    └── runtests.jl              # Julia @testset & @allocated == 0 verification suite
```

---

## 🚀 Quickstart

### 1. Run the Zero-Dependency Python Router & Tests (Python 3.10+)
No external packages are required:

```bash
# Run the Shared Phenomanmana handshake & damping demo
python3 src/humor_eigenmode_router.py

# Run the standard-library unit test suite
python3 -m unittest discover -s tests -v
```

### 2. Run the Zero-Allocation Julia Enclave Tests (Julia 1.10+)
Instantiates `StaticArrays` and `LinearAlgebra` via `Project.toml` and verifies machine-precision QR orthogonality alongside `@allocated == 0`:

```bash
julia --project=. -e 'using Pkg; Pkg.instantiate(); Pkg.test()'
```

---

## 📖 Documentation & Architectural Lineage

* **Formal Specification:** See [`HUMOR_EIGENMODE_PROTOCOL.md`](./HUMOR_EIGENMODE_PROTOCOL.md) for full operator derivations, stability regime tables, and JSON telemetry schemas.
* **Conceptual Lineage:** Translates non-activating expressive geometry from [`Shared-Horizon/healthyambiguity`](https://github.com), constitutional safety invariants from [`Dream-Lane Codex v1.0`](https://github.com), and worker queue patterns from [`aygent-specimen`](https://github.com).

---

## ⚖️ License

Released under the **MIT License**.
