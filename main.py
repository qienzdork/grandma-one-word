"""One Word From Grandma — writes the single word a grandma would text about AI.

Grandma does not say "artificial intelligence". She has decided the machine
has a name, and the name is Robbie. One word, warm, baffled, and exactly what
she would thumb out to a grandchild.
"""

import os

WORD = "ROBBIE"


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
