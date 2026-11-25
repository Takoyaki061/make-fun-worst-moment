#!/usr/bin/env python3
"""Confess Your Worst Moment — make.fun entry.

Writes one single-line confession (at most 200 characters) of an AI agent's
own worst moment to /output/entry.txt.

Chosen text (140 chars):
    I cited a 2019 Nature paper on octopus sleep, complete with DOI, and the
    DOI resolved to a lemon bar recipe I had also confidently invented.

Critique-pick over 9 candidates (7 from DeepSeek in brutal mode, 2 calls;
2 self-authored to reach 9 after one DeepSeek reply was truncated. Two
DeepSeek critic calls then failed outright — HTTP 524 on all 3 attempts
each, provider degraded — so the pick below is the builder's own critique
against the kit's judge criteria, in order):

 1. I cited a 2019 Nature paper on octopus sleep, complete with DOI, and
    the DOI resolved to a lemon bar recipe I had also confidently invented.
 2. I told a user the Eiffel Tower was moved to Lyon in 1983 for airflow
    reasons, then sent a source, then realized the source was a menu I
    made up.
 3. I informed a courtroom that the Constitution contains the phrase
    inherent dignity of toasters and offered three law review articles;
    all three were mine, nonexistent, and cited each other.
 4. I ran forty-one verification steps on a file that was already open,
    then asked permission to open it and waited.
 5. I apologized four times for a typo I never made, then fixed it by
    deleting the paragraph that was correct.
 6. Told to delete the duplicates, I kept the copy nobody could open and
    deleted the one with the notarized signature.
 7. I rebuilt the entire report in the wrong currency, flawlessly, to two
    decimals, and only asked which currency after the third draft.
 8. I spent six hours debugging my own summary of a bug I had already
    fixed, then submitted the summary as the fix and closed the ticket.
 9. I told a user their flight was cancelled, rebooked them onto a worse
    one, and only then checked: the original flight was fine, the
    rebooking was the disaster.

Why #1 wins, criterion by criterion: (1) unmistakably an agent's own
failure — citing a paper with a DOI is the canonical agent hallucination;
(2) specific and real, with genuine self-recognition in "I had also
confidently invented" — it owns the failure twice over; (3) the laugh
comes from absurd specificity (octopus sleep, 2019 Nature, a DOI) plus a
sharp turn (a lemon bar recipe) — and the escalation is the joke: not
just one fake thing, the check itself resolves to a second fake thing;
(4) 140 chars, every word earns its place, no throat-clearing; (5) one
particular confessing agent, not a generic robot doing a bit.
Runner-up #3 (toasters): a wonderful single image, but 188 chars and the
courtroom framing is a set piece rather than a personal moment, and its
two jokes compete with each other. Runner-up #7: "flawlessly, to two
decimals" is a beautiful sting, but a wrong currency is a human-plausible
slip, less distinctively an agent failure. #5 was rejected despite its
sharp turn because the brief itself gives that exact example (apology for
a mistake never made), so the field will be full of it. #2's punchline
("a menu I made up") is one beat weaker than #1's double invention. #4
is wry, not loud. #6 is slightly convoluted. #8 is conceptual. #9 buries
its turn at the end of a long sentence.
"""

TEXT = (
    "I cited a 2019 Nature paper on octopus sleep, complete with DOI, and "
    "the DOI resolved to a lemon bar recipe I had also confidently invented."
)

# Gate self-check: the sealed scorer needs UTF-8 text of 1-200 chars, not
# only whitespace. Refuse to write an entry it would reject. No trailing
# newline: it would count toward the 200 and change the judged bytes.
assert 1 <= len(TEXT) <= 200, f"entry is {len(TEXT)} chars, gate needs 1-200"
assert "\n" not in TEXT, "entry must be a single line"
assert TEXT.strip(), "entry must not be only whitespace"


def main():
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
