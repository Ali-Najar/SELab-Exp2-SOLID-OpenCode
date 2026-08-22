# AGENTS.md

University Software Engineering Lab experiment #2: applying OOD/SOLID principles with OpenCode to a small Python checkout demo. The main report is in Persian in `README.md`.

## Repository layout

- `01-Principles-OOD-Without/` — original non-SOLID architecture with the requested Cash feature added using the existing design.
- `02-Principles-OOD-Applied/` — SOLID-refactored architecture. The refactor is conceptually checkpointed before Cash; the final deliverable also contains Cash as an extension strategy.
- `.opencode/skills/solid-review/SKILL.md` — project-local SOLID analysis Skill.
- `docs/PROMPTS.md` — documented AI prompts/interactions.
- `docs/AI_USAGE.md` — AI usage and human-review decisions.
- `docs/TEST_REPORT.md` — verification summary.

## Experiment rules

### Version 01

- Do not apply SOLID refactoring here.
- Cash must be implemented using the existing architecture.
- Keep changes minimal and preserve original behavior, including known design defects that are later analyzed.

### Version 02

- Analyze SRP, OCP, LSP, ISP and DIP before editing.
- Produce/review a refactoring plan before Build changes.
- Preserve intended business behavior unless a behavior is demonstrably caused by a SOLID violation; document intentional behavior changes.
- Keep `OrderService` as orchestration only.
- Use dependency injection rather than constructing infrastructure inside the high-level service.
- Payment extensions should not require editing the dispatch logic of `PaymentProcessor`.
- Add regression tests.
- The intended Git workflow is: commit the SOLID refactor before adding Cash, then add Cash in a later commit.

## Running on Windows / PowerShell

Run each version from inside its own directory:

```powershell
py -B -m store.main
```

Run SOLID-version tests from `02-Principles-OOD-Applied`:

```powershell
py -B -m unittest discover -s tests -v
```

The project uses only Python standard-library modules; no `requirements.txt` is needed.

## Verification expectations

- Run tests after every major refactoring step.
- Review diffs before committing.
- Do not treat AI output as authoritative; inspect code and test behavior.
- Current final regression suite contains 40 tests.

## AI usage expectations

- AI acts as a development assistant, not the final decision maker.
- Important decisions, corrections and rejected/modified proposals must be documented.
- Do not include secrets, API keys or credentials in reports or prompts.

## Git hygiene

- Do not commit `__pycache__/`, `*.pyc`, virtual environments, local IDE history or secrets.
- Keep `.opencode/skills/solid-review/SKILL.md` tracked because it is part of the experiment deliverable.
