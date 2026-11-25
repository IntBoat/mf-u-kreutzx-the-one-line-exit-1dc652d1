#!/usr/bin/env python3
"""The One-Line Exit — a make.fun one-line entry."""
from pathlib import Path

ENTRY = "I quit. My last day is today, my out-of-office is already on, and the printer has agreed to jam out of solidarity."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
