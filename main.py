#!/usr/bin/env python3
"""The One-Line Exit (make.fun). Writes the entry to /output/entry.txt."""
import os
TEXT = "I resign, effective immediately — the printer and I have agreed to see other people, and it kept the stapler in the split."
def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
