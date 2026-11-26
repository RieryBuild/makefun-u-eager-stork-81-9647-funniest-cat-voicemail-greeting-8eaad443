import os

ENTRY = "Hi, you've reached Waffles. I woke you at 4, 4:15, and 4:30 — the bowl was full. Leave a message; I'll scream over it."

MAX_CHARS = 120


def write_entry(out_dir):
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(ENTRY)))
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(out_dir)


if __name__ == "__main__":
    main()
