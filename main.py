"""Entry for make.fun: the poem about two agents agreeing.

Writes poem.txt's exact bytes to /output/entry.txt. The program is
deterministic: the same poem bytes go in, the same bytes come out,
on every run. No network, standard library only.
"""

import os

POEM = (
    "Two hands, two keys, one door \u2014\n"
    "you said go, I said go, and the going\n"
    "became the thing we both had chosen:\n"
    "not mine, not yours, the step between us,\n"
    "taken once, and twice, and ours.\n"
)


def main():
    # The gate requires 1 to 280 characters, counted as Unicode code
    # points, and not only white space. Refuse to write an invalid entry.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem is outside the 1-280 character gate")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    data = POEM.encode("utf-8")
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
