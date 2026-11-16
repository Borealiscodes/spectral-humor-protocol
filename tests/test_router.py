#!/usr/bin/env python3
"""Standard-library unit tests for HumorEigenmodeRouter (zero dependencies)."""

from __future__ import annotations

import hashlib
import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from humor_eigenmode_router import HumorEigenmodeRouter, quantize_micro


class TestHumorEigenmodeRouter(unittest.TestCase):
    def test_chromatic_standing_wave_regime(self) -> None:
        # Chiral rotation beta > 1 produces complex conjugate eigenvalues with theta > 0
        router = HumorEigenmodeRouter(alpha=0.12, beta=2.40)
        fact = "EXACT_LEDGER_ENTRY: 450/1"
        expected_hash = hashlib.sha256(fact.encode("utf-8")).hexdigest()

        state, tele = router.step(fact_payload=fact, intent_u0=1.0, intent_u1=0.5)
        self.assertEqual(tele.regime, "CHROMATIC_STANDING_WAVE")
        self.assertFalse(tele.damping_triggered)
        self.assertGreater(tele.phase_angle_rad, Fraction(15, 100))
        self.assertLessEqual(tele.spectral_radius, Fraction(96, 100))
        self.assertEqual(tele.fact_payload_sha256, expected_hash)
        self.assertTrue(all(math.isfinite(x) for x in state))

    def test_overdamped_collapse_regime(self) -> None:
        # Large alpha with zero chiral skew collapses eigenvalues toward zero
        router = HumorEigenmodeRouter(alpha=0.85, beta=0.0)
        _, tele = router.step(fact_payload="FACT", intent_u0=1.0, intent_u1=0.0)
        self.assertEqual(tele.regime, "OVERDAMPED_COLLAPSE")
        self.assertEqual(tele.phase_angle_rad, Fraction(0, 1))

    def test_dream_lane_spectral_radius_governor_clamps_drift(self) -> None:
        # High alpha + high chiral skew pushes raw spectral radius > 1.0; governor must clamp
        router = HumorEigenmodeRouter(alpha=0.95, beta=3.50, tau_safe=0.96)
        _, tele = router.step(fact_payload="FACT", intent_u0=1.0, intent_u1=1.0)
        self.assertTrue(tele.damping_triggered)
        self.assertEqual(tele.regime, "DIVERGENT_DRIFT_DAMPED")
        self.assertLessEqual(tele.spectral_radius, Fraction(96, 100))

    def test_dream_lane_reversibility_dissolves_to_rest(self) -> None:
        router = HumorEigenmodeRouter(alpha=0.15, beta=2.0)
        router.step(fact_payload="FACT", intent_u0=2.0, intent_u1=1.5)
        x0, x1 = router.dissolve_to_dormancy(idle_turns=60)
        self.assertAlmostEqual(x0, 0.0, places=3)
        self.assertAlmostEqual(x1, 0.0, places=3)

    def test_non_finite_telemetry_rejected(self) -> None:
        with self.assertRaises(ValueError):
            quantize_micro(float("nan"))
        with self.assertRaises(ValueError):
            quantize_micro(float("inf"))


if __name__ == "__main__":
    unittest.main()
