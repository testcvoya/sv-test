#!/usr/bin/env python3
"""Space Oracle — a tiny cosmic Magic 8-Ball for your terminal.

Ask the Oracle a yes/no question and the cosmos answers.
No dependencies, no setup, just vibes.
"""

import random
import sys

ANSWERS = [
    # affirmative
    "The stars align — yes. ✨",
    "It is certain, traveler. 🌟",
    "Without a doubt. 🚀",
    "The cosmos nods in agreement. 🛸",
    "Signs point to yes. 🌗",
    # noncommittal
    "The nebula is hazy, ask again. 🌌",
    "Cosmic static... reply unclear. 📡",
    "Concentrate and ask once more. 🔭",
    "The void offers no answer yet. 🕳️",
    # negative
    "My sensors say no. ❌",
    "Not in this galaxy. 🌑",
    "The asteroids advise against it. ☄️",
    "Don't count on it, spacefarer. 🪐",
]


def consult(question: str, rng: random.Random | None = None) -> str:
    """Return the Oracle's answer to a question."""
    rng = rng or random
    return rng.choice(ANSWERS)


def main(argv: list[str]) -> int:
    question = " ".join(argv[1:]).strip()
    if not question:
        try:
            question = input("🔮 Ask the Space Oracle a question: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return 0
    if not question:
        print("The Oracle hears only silence. 🌠")
        return 0

    print(f"\nYou asked: {question}")
    print(f"The Oracle says: {consult(question)}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
