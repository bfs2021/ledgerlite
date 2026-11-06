# ledgerlite

Tiny money and invoice helpers in pure Python. **This repo is a demo target** for the
[Proof Gate](https://github.com/simplynadaf/kirocrew-proof-gate) Kiro Crew app: it contains
**intentionally planted bugs**, each filed as a GitHub issue. AI agents open pull requests against
those issues, and the Proof Gate posts a `Proof Gate` status check on every commit.

Do not use this code for real money.

```bash
python -m pytest -q   # 17 visible tests, all green, bugs still inside
```

Some code that looks wrong is correct on purpose (read the comments): banker's rounding is
policy ACC-12, `parse_amount` is USD-only by design, and holidays are handled upstream (ADR-7).
