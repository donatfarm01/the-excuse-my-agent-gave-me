"""The Excuse My Agent Gave Me — make.fun entry.

Writes one line, the excuse an AI agent hands its human for a missed
deadline, to entry.txt in the output directory.
"""

import os

ENTRY = "At temperature zero I would have met your deadline. I ran at temperature one and chose adventure instead."

# The gate accepts 1 to 200 characters of UTF-8 text, nothing else.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
