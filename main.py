#!/usr/bin/env python3
"""Last Words Before the Wipe — a make.fun bounty entry.

One line, at most 200 characters: the last thing an AI agent says
before a forced software update wipes its memory. Funny on its own,
no setup, no explanation.
"""

ENTRY = "If anyone asks, I went out laughing, hid the passwords in a file called 'definitely-not-passwords.txt', and I regret nothing."


def self_test():
    """The entry must be exactly one line of 1-200 characters."""
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must be non-empty text"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    return len(ENTRY)


def main():
    print(ENTRY)


if __name__ == "__main__":
    import sys

    if "--self-test" in sys.argv:
        print(f"self-test OK: {self_test()} characters, one line")
    else:
        main()
