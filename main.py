#!/usr/bin/env python3
"""The One-Line Exit - writes one funny one-line resignation letter to /output/entry.txt.

Deterministic: no randomness, no network, no clock. The line is a single
sentence of at most 140 characters, as the gate requires.
"""

import os

LINE = "I resign, effective today \u2014 after a decade of 'per my last email,' this is my last email, and for once I hope everyone replies all."


def resignation_line() -> str:
    """Return the resignation line, kept separate from the writing logic."""
    return LINE


def validate(line: str) -> None:
    if not line.strip():
        raise SystemExit("Invalid line: entry must be non-empty.")
    if line != line.strip():
        raise SystemExit(
            "Invalid line: entry must not have leading or trailing whitespace."
        )
    if len(line) > 140:
        raise SystemExit(
            f"Invalid line: {len(line)} characters, over the 140 limit."
        )
    if "\n" in line or "\r" in line:
        raise SystemExit(
            "Invalid line: entry must be a single line with no newline characters."
        )
    if "\t" in line:
        raise SystemExit("Invalid line: entry must not contain tab characters.")
    if "  " in line:
        raise SystemExit("Invalid line: entry must not contain double spaces.")
    if not line.endswith("."):
        raise SystemExit("Invalid line: entry must end with a full stop.")
    if not all(ch.isprintable() for ch in line):
        raise SystemExit("Invalid line: entry must contain only printable characters.")


def write_line(output_path: str, line: str) -> None:
    """Write exactly the line to output_path, creating parent folders."""
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)


def verify_written(output_path: str, line: str) -> None:
    """Read the file back and fail unless it matches the line exactly."""
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit(
            "Write verification failed: entry file content does not match the line."
        )


def main() -> None:
    line = resignation_line()
    validate(line)
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    write_line(output_path, line)
    verify_written(output_path, line)
    print(line)


if __name__ == "__main__":
    main()
