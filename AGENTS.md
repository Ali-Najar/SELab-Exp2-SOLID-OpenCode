# AGENTS.md

University SE-lab experiment (#2): applying OOD/SOLID principles with OpenCode to a small `store` checkout demo. README is in Persian.

## Layout & experiment rules

Two independent versions of the same project (`models`, `order_service`, `pricing`, `payment`, `notification`, `storage`, `main`; entry point is `store/main.py`):

- `01-Principles-OOD-Without/store/` — the original non-SOLID architecture. Do **not** apply SOLID refactoring here. Its only planned change: implement cash payment **using the existing design**, with minimum changes that preserve existing behavior. Explain proposed changes before applying them.
- `02-Principles-OOD-Applied/store/` — starts from the same baseline **without cash**. Workflow order matters:
  1. Analyze SRP, OCP, LSP, ISP, DIP on the baseline.
  2. Produce a refactoring plan before making major changes.
  3. Apply the SOLID refactor and add regression tests.
  4. Commit this checkpoint **before** adding cash.
  5. Only then implement cash payment.
- Avoid unnecessary abstractions and overengineering; preserve intended business behavior in both trees.

## Running

Run each experiment **from inside its folder**:

```
python -m store.main
```

`python store/main.py` or running from the repo root fails with `ModuleNotFoundError` (packages rely on namespace packages; there is no `__init__.py`).

## Verification

- Pure stdlib Python (no `requirements.txt`, no venv needed). Verified with Python 3.13.
- No lint/typecheck/CI exists. Verify by running the demo and checking the printed receipts/output, plus the regression tests added under `02`.
- Verify after every major refactoring step.

## AI usage expectations (assignment)

- AI is a development assistant, not the final decision maker: explain important architectural decisions and report uncertainties.
- Do not silently change business rules.

## Git gotchas

- `.gitignore` only covers macOS/VSCode — it has no Python entries, so `__pycache__/` shows up as untracked after any run (exists in both trees already). Never commit it.
- Checkpoint commits are part of the required workflow in `02` (SOLID refactor committed before cash); otherwise don't commit without being asked.
