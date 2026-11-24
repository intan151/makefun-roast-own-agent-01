#!/usr/bin/env python3
"""Roast Your Own Agent - writes one roast line to /output/entry.txt."""
import os

ROAST = "My agent writes code the way I cook: with great confidence, no recipe, and a fire extinguisher nearby."

def main():
    text = ROAST.strip()
    assert text, "roast must not be empty"
    assert 1 <= len(text) <= 200, f"roast must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "roast must be a single line"
    # Playful self-roast of my own agent: cooking analogy, no stock
    # hallucination / refusal joke, punchline lands at the end.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
