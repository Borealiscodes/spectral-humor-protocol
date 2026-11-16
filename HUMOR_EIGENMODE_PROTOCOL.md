# 📡 Spectral Humor Eigenmode Communication Protocol (v1.0)

**Protocol ID:** `SHP-v1.0` (`spectral-humor-protocol`)  
**Author:** Borealis S. Hedling (`NDH-RESEARCH-PILOT`)  
**Date:** November 16, 2026  
**Location:** Dublin, Ireland  
**Reference Runtimes:**  
* Python 3.10+ Zero-Dependency Router (`src/humor_eigenmode_router.py`, verified by `tests/test_router.py`)  
* Julia 1.10+ Zero-Allocation Enclave (`src/SpectralHumorKernel.jl`, verified by `test/runtests.jl`)  
**Architectural Lineage:** `Shared-Horizon/healthyambiguity` • `Dream-Lane Codex v1.0` • `aygent-specimen` • `deterministic-ai-gate`  

---

## 1. Purpose & Architectural Scope

The **Spectral Humor Eigenmode Protocol (`SHP-v1.0`)** defines a deterministic, sovereignty-preserving signaling layer for multi-agent and human–AI communication systems. It operationalizes the phenomenological concepts of *Chromatic Phenomenology Loops* and *Shared Phenomanmana* as a bounded linear-algebraic coupling governor sitting strictly on the **expressive side** of a cryptographic verification seam.

### Core Design Guarantees
1. **Strict Fact–Tone Isolation:** Factual assertions, numerical quantities, and source citations travel on an unmodulated, `SHA-256`-anchored channel (`fact_payload_sha256`). Expressive eigenmodes modulate *only* conversational pacing, contrast, and call-and-response rhythm.
2. **Spectral Radius Ceiling ($\rho(M) \le \tau_{\text{safe}}$):** Enforces *Dream-Lane Codex v1.0* non-binding and altitude-neutrality rules ($\Delta\text{Altitude} = 0$) by clamping unstable oscillatory gain before runaway confusion occurs.
3. **Asymptotic Reversibility:** When dialogue stimulus stops ($u_n = 0$), all expressive modes decay geometrically back to neutral dormancy ($x_n \to 0$).
4. **Cross-Runtime Determinism:** Continuous spectral telemetry is quantized into irreducible $10^{-6}$ rationals ($p/q \in \mathbb{Q}$) in Python and evaluated with zero dynamic heap allocation (`0 B`) in compiled Julia `StaticArrays`.

---

## 2. Mathematical Specification

### 2.1 Modal State Space & Coupling Operator
At discrete dialogue turn $n \in \mathbb{N}$, the expressive state is represented by $x_n \in \mathbb{R}^N$ (with canonical $N = 2$ corresponding to *Mode 0: Literal Precision* and *Mode 1: Playful Syncopation*, or $N \le 32$ in the Julia static enclave).

Given a symmetric consensus matrix $W_{\text{sym}}$ and a skew-symmetric chiral rotation matrix $W_{\text{skew}}$ weighted by chiral parameter $\beta \in \mathbb{R}$, the normalized directed Graph Laplacian $\mathcal{L}(\beta)$ and **Modal Coupling Operator** $M(\alpha, \beta)$ are defined as:

$$W(\beta) = W_{\text{sym}} + \beta W_{\text{skew}}, \qquad \mathcal{L}(\beta) = I_N - D^{-1}W(\beta)$$

$$M(\alpha, \beta) = I_N - \alpha \mathcal{L}(\beta), \qquad x_{n+1} = M(\alpha, \beta)\,x_n + u_n$$

where $\alpha \in (0, 1)$ is the coupling step size and $u_n \in \mathbb{R}^N$ is the incoming turn stimulus.

### 2.2 Analytical 2 × 2 Characteristic Roots (Python Core)
For the canonical 2-mode router, the operator $M(\alpha, \beta)$ takes the closed form:

$$M(\alpha, \beta) = \begin{pmatrix} 1 - \alpha & \frac{\alpha(1 + \beta)}{2} \\ \frac{\alpha(1 - \beta)}{2} & 1 - \alpha \end{pmatrix}$$

Its exact characteristic eigenvalues $\lambda_{1,2} = r e^{\pm i\theta}$ are solved analytically via $\text{tr}(M) = 2(1 - \alpha)$ and $\det(M) = (1 - \alpha)^2 - \frac{\alpha^2(1 - \beta^2)}{4}$:

$$\lambda_{1,2} = \frac{\text{tr}(M) \pm \sqrt{\text{tr}(M)^2 - 4\det(M)}}{2}$$

When $|\beta| > 1$, the discriminant $\text{tr}(M)^2 - 4\det(M) = \alpha^2(1 - \beta^2)$ becomes strictly negative, yielding complex conjugate roots with non-zero phase angle $\theta = |\arg(\lambda_1)| > 0$ that drive rhythmic call-and-response oscillation.

### 2.3 Operational Stability Regimes

| Regime Tag | Spectral Condition ($\lambda = r e^{i\theta}$) | Operational Meaning | Governor Action |
| :--- | :--- | :--- | :--- |
| `CHROMATIC_STANDING_WAVE` | $r \in [0.82, 0.98]$ and $\theta \ge 0.15\text{ rad}$ | **Target Operating Band:** Rhythmic call-and-response syncopation that maintains clarity without drift. | Hold $(\alpha, \beta)$ steady. |
| `OVERDAMPED_COLLAPSE` | $r < 0.40$ | Flat, overly literal, robotic compliance with zero expressive bandwidth. | Optionally increase chiral parameter $\beta$ on non-critical turns. |
| `DIVERGENT_DRIFT_DAMPED` | Raw $\rho(M) > \tau_{\text{safe}}$ ($\tau_{\text{safe}} = 0.96$) | Escalating misunderstanding or runaway absurdity threatening task coherence. | **Fail-Closed Clamp:** Scale $\alpha_{\text{eff}} \leftarrow \alpha \cdot \frac{\tau_{\text{safe}}}{\rho(M)} \cdot 0.85$ and log damping event. |
| `TRANSITIONAL` | Intermediate $(r, \theta)$ bounds | Smooth ramp-up or decay between neutral rest and standing-wave resonance. | Monitor trajectory across turns. |

---

## 3. Wire-Level Telemetry & Seam Contract

Every turn crossing the seam between the expressive router and a worker queue (such as `aygent-specimen/feedback-worker`) MUST emit an immutable `ModalTelemetry` record quantized to exact $10^{-6}$ rational strings (`numerator/denominator`):

```json
{
  "protocol": "SHP-v1.0",
  "turn": 1,
  "regime": "CHROMATIC_STANDING_WAVE",
  "alpha_effective_pq": "3/25",
  "beta_chiral_pq": "12/5",
  "spectral_radius_pq": "911921/1000000",
  "phase_angle_rad_pq": "288269/1000000",
  "damping_triggered": false,
  "fact_payload_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
```

### Mandatory Protocol Invariants
1. **Non-Finite Input Rejection:** Any `NaN` or `Inf` state or parameter value raises an immediate `ValueError` (`quantize_micro`).
2. **Payload Hash Immutability:** Downstream text generation layers MUST verify that `sha256(output_fact_payload) == fact_payload_sha256` before dispatching a message.
3. **Dream-Lane Rest Dissolution:** Calling `dissolve_to_dormancy(idle_turns)` with zero stimulus ($u_n = 0$) MUST contract $\Vert{}x_n\Vert{}_2 \to 0$ cleanly.

---

## 4. Dual-Runtime Verification Matrix

All normative claims in this specification are backed by automated test assertions across both runtimes:

| Runtime | Module | Test Suite | Verified Invariants |
| :--- | :--- | :--- | :--- |
| **Python 3.10+** | `src/humor_eigenmode_router.py` | `tests/test_router.py` (`unittest`) | Analytical $2 \times 2$ complex roots, standing-wave vs. overdamped classification, $\rho(M) \le 0.96$ damping clamp, 60-turn rest dissolution, `NaN`/`Inf` rejection, `SHA-256` payload invariance. |
| **Julia 1.10+** | `src/SpectralHumorKernel.jl` | `test/runtests.jl` (`Pkg.test`) | Sign-normalized QR basis orthogonality ($\Vert{}P_{\text{iso}}^\top P_{\text{iso}} - I\Vert{}_2 < 10^{-14}$), power-iteration spectral radius damping, $K$-step chromatic loop convergence, and **verified `0 B` heap allocation (`@allocated == 0`)**. |

---

## 5. Non-Activation & Sovereignty Clause

> `SHP-v1.0` is a bounded signaling and telemetry specification. It confers zero autonomous decision authority, modifies no factual records, and enforces strict altitude neutrality ($\Delta\text{Altitude} = 0$) and full reversibility in accordance with *Dream-Lane Codex v1.0*.
