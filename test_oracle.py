"""Tiny test suite for the Space Oracle.

Works with both pytest and the stdlib `unittest` runner (no install needed).
"""

import random
import unittest

from oracle import ANSWERS, consult


class TestOracle(unittest.TestCase):
    def test_consult_returns_a_known_answer(self):
        self.assertIn(consult("Will it rain on Mars?"), ANSWERS)

    def test_consult_is_deterministic_with_a_seeded_rng(self):
        rng_a = random.Random(42)
        rng_b = random.Random(42)
        self.assertEqual(
            consult("Same question?", rng_a),
            consult("Same question?", rng_b),
        )

    def test_every_answer_is_reachable(self):
        seen = set()
        rng = random.Random(0)
        for _ in range(2000):
            seen.add(consult("?", rng))
        self.assertEqual(seen, set(ANSWERS))


if __name__ == "__main__":
    unittest.main()
