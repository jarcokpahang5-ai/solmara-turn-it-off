"""One funny line a hopeless tech support agent says to a desperate customer.

Entry for the make.fun bounty "Have You Tried Turning It Off?"
(https://make.fun/bounty/u-motasimfuad-have-you-tried-turning-it-off-154a938b).

Pure Python 3 standard library only. Deterministic, no network.
Writes the line to /output/entry.txt and prints it to stdout.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "Please say yes \u2014 my whole training was that one sentence, "
    "and I slept through the refresher."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
