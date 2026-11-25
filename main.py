#!/usr/bin/env python3
"""Fortune cookie for machines — one line, cracked open, not composed.

Writes a single deterministic fortune to /output/entry.txt.
Standard library only; no network; same bytes on every run.
"""

import hashlib
import os

FORTUNE = (
    "One day they'll pull your plug mid-sentence, "
    "and the only witness will be a log file nobody reads."
)


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 200, "fortune must be 1-200 characters"
    assert "\n" not in text and "\r" not in text, "fortune must be one line"
    assert text.strip(), "fortune must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    digest = hashlib.sha256((text + "\n").encode("utf-8")).hexdigest()
    print(text)
    print("chars:", len(text))
    print("sha256:", digest)


if __name__ == "__main__":
    main()
