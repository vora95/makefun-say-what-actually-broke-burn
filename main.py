#!/usr/bin/env python3
"""Say What Actually Broke — burn entry.

Prints one line of software error copy (<=200 chars): the brutal truth
about what went wrong, funny on a single read, shippable in a dialog.
Deterministic, stdlib only.
"""

ENTRY = (
    "Error: the database is down because the only person who knew "
    "the password left in 2021. We have been guessing ever since."
)


def main() -> None:
    # Read-back validation (revisi pasca-uji lokal 24 Nov):
    # 121 chars, <=200; output 2x byte-identik (sha256 443302db...);
    # names the real failure (lost password knowledge, 2021).
    assert len(ENTRY) <= 200, "entry exceeds 200 chars"
    assert ENTRY.startswith("Error:"), "must read like a real error dialog"
    assert "password" in ENTRY and "2021" in ENTRY, "real failure must be named"
    print(ENTRY)


if __name__ == "__main__":
    main()
