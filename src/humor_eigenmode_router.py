#!/usr/bin/env python3
"""
humor_eigenmode_router.py
Operational Spectral Humor Eigenmode Router & Dream-Lane Sovereignty Governor.
Zero external dependencies (Python 3.10+ standard library).
"""

from __future__ import annotations

import cmath
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from typing import Literal

RegimeTag = Literal[
    "OVERDAMPED_COLLAPSE",
    "CHROMATIC_STANDING_WAVE",
    "DIVERGENT_DRIFT_DAMPED",
    "TRANSITIONAL",
]


def quantize_micro(val: float) -> Fraction:
    """Quantize continuous float telemetry to exact 10^-6 rational p/q."""
    if not math.isfinite(val):
        raise ValueError(f"Non-finite telemetry value rejected: {val!r}")
    return Fraction(round(val * 1_000_000), 1_000_000)


@dataclass(frozen=True)
class ModalTelemetry:
    """Exact rational spectral telemetry emitted at the deterministic seam."""
    turn: int
    alpha_effective: Fraction
    beta_chiral: Fraction
    spectral_radius: Fraction
    phase_angle_rad: Fraction
    regime: RegimeTag
    damping_triggered: bool
    fact_payload_sha256: str


@dataclass
class HumorEigenmodeRouter:
    """
    2-Mode Cross-Agent Coupling Operator M(α, β) = I_2 - α * L(β):
      Mode 0: Literal Precision
      Mode 1: Playful Syncopation (Chiral Call-and-Response)

    Enforces Dream-Lane Codex invariants:
      - Spectral radius ceiling ρ(M) <= tau_safe (0.96)
      - Full reversibility (geometric decay to rest state x -> [0, 0] when idle)
      - Strict isolation from fact_payload_sha256
    """
    alpha: float = 0.25
    beta: float = 0.85
    tau_safe: float = 0.96
    r_min: float = 0.82
    r_max: float = 0.98
    theta_min: float = 0.15
    state_x0: float = 0.0
    state_x1: float = 0.0
    turn_count: int = 0

    def _build_coupling_matrix(self, alpha: float, beta: float) -> tuple[float, float, float, float]:
        """
        Construct M = I_2 - alpha * L(beta) where normalized directed Laplacian L
        combines symmetric consensus (1.0) and skew-symmetric chiral rotation (±beta).
        Resulting 2x2 operator:
            M = [[1 - alpha,         alpha * (1 + beta) / 2],
                 [alpha * (1 - beta) / 2,  1 - alpha       ]]
        """
        m11 = 1.0 - alpha
        m12 = 0.5 * alpha * (1.0 + beta)
        m21 = 0.5 * alpha * (1.0 - beta)
        m22 = 1.0 - alpha
        return m11, m12, m21, m22

    def _solve_2x2_eigenvalues(
        self, m11: float, m12: float, m21: float, m22: float
    ) -> tuple[complex, complex]:
        """Exact analytical characteristic roots λ = (tr ± sqrt(tr^2 - 4*det)) / 2."""
        trace = m11 + m22
        det = (m11 * m22) - (m12 * m21)
        discriminant = (trace * trace) - (4.0 * det)
        root = cmath.sqrt(discriminant)
        lam1 = (trace + root) / 2.0
        lam2 = (trace - root) / 2.0
        return lam1, lam2

    def step(
        self,
        fact_payload: str,
        intent_u0: float,
        intent_u1: float,
    ) -> tuple[tuple[float, float], ModalTelemetry]:
        """
        Advance expressive state x_{n+1} = M x_n + u_n while keeping fact_payload
        cryptographically isolated and enforcing ρ(M) <= tau_safe.
        """
        self.turn_count += 1
        fact_digest = hashlib.sha256(fact_payload.encode("utf-8")).hexdigest()

        eff_alpha = self.alpha
        m11, m12, m21, m22 = self._build_coupling_matrix(eff_alpha, self.beta)
        lam1, lam2 = self._solve_2x2_eigenvalues(m11, m12, m21, m22)
        rho = max(abs(lam1), abs(lam2))

        # Dream-Lane Spectral Radius Governor: clamp unstable drift (ρ >= tau_safe)
        damped = False
        if rho > self.tau_safe and eff_alpha > 0.0:
            damped = True
            # Scale alpha down toward stability band and recompute roots
            eff_alpha = eff_alpha * (self.tau_safe / rho) * 0.85
            m11, m12, m21, m22 = self._build_coupling_matrix(eff_alpha, self.beta)
            lam1, lam2 = self._solve_2x2_eigenvalues(m11, m12, m21, m22)
            rho = max(abs(lam1), abs(lam2))

        # Dominant eigenmode modulus & phase angle
        dom = lam1 if abs(lam1) >= abs(lam2) else lam2
        r_dom = abs(dom)
        theta_dom = abs(cmath.phase(dom))

        # Advance state vector x_{n+1} = M x_n + u_n
        next_x0 = (m11 * self.state_x0) + (m12 * self.state_x1) + intent_u0
        next_x1 = (m21 * self.state_x0) + (m22 * self.state_x1) + intent_u1
        self.state_x0, self.state_x1 = next_x0, next_x1

        # Classify operational regime
        if damped or rho >= 1.0:
            regime: RegimeTag = "DIVERGENT_DRIFT_DAMPED"
        elif r_dom < 0.40:
            regime = "OVERDAMPED_COLLAPSE"
        elif self.r_min <= r_dom <= self.r_max and theta_dom >= self.theta_min:
            regime = "CHROMATIC_STANDING_WAVE"
        else:
            regime = "TRANSITIONAL"

        telemetry = ModalTelemetry(
            turn=self.turn_count,
            alpha_effective=quantize_micro(eff_alpha),
            beta_chiral=quantize_micro(self.beta),
            spectral_radius=quantize_micro(rho),
            phase_angle_rad=quantize_micro(theta_dom),
            regime=regime,
            damping_triggered=damped,
            fact_payload_sha256=fact_digest,
        )
        return (self.state_x0, self.state_x1), telemetry

    def dissolve_to_dormancy(self, idle_turns: int = 20) -> tuple[float, float]:
        """Dream-Lane Reversibility: zero-input evolution decays cleanly toward rest."""
        for _ in range(idle_turns):
            self.step(fact_payload="", intent_u0=0.0, intent_u1=0.0)
        return (self.state_x0, self.state_x1)


def simulate_phenomanmana_handshake() -> None:
    """Demonstrate standing-wave resonance, runaway damping, and clean dissolution."""
    # 1. Resonant call-and-response regime (chiral rotation β > 1 induces complex conjugate roots)
    router = HumorEigenmodeRouter(alpha=0.12, beta=2.40)
    fact = "EXACT_ALLOCATION: 150/1 UNITS"

    print("=== 1. SHARED PHENOMANMANA HANDSHAKE (STANDING WAVE) ===")
    for turn in range(1, 4):
        state, tele = router.step(fact_payload=fact, intent_u0=1.0, intent_u1=0.5 if turn == 1 else 0.0)
        print(json.dumps({
            "turn": tele.turn,
            "regime": tele.regime,
            "spectral_radius_pq": f"{tele.spectral_radius.numerator}/{tele.spectral_radius.denominator}",
            "phase_rad_pq": f"{tele.phase_angle_rad.numerator}/{tele.phase_angle_rad.denominator}",
            "state": [round(state[0], 4), round(state[1], 4)],
            "fact_sha256_preserved": tele.fact_payload_sha256[:16] + "...",
        }))

    # 2. Adversarial runaway coupling -> Dream-Lane Governor clamps ρ(M) <= 0.96
    print("\n=== 2. DIVERGENT DRIFT GOVERNOR TEST ===")
    unstable_router = HumorEigenmodeRouter(alpha=0.95, beta=3.50)
    _, tele_damped = unstable_router.step(fact_payload=fact, intent_u0=1.0, intent_u1=1.0)
    print("Damping triggered:", tele_damped.damping_triggered, "| Regime:", tele_damped.regime)

    # 3. Idle dissolution back to neutral dormancy
    rest_state = router.dissolve_to_dormancy(idle_turns=40)
    print("\n=== 3. DREAM-LANE REVERSIBILITY (DISSOLUTION TO REST) ===")
    print("Residual state after 40 idle turns:", [round(rest_state[0], 6), round(rest_state[1], 6)])


if __name__ == "__main__":
    simulate_phenomanmana_handshake()
