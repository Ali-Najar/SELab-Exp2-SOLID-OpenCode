---
name: solid-review
description: Analyze Python object-oriented code for SOLID violations and propose safe incremental refactoring.
---

# SOLID Review Skill

When analyzing a Python object-oriented project:

1. Read all relevant source files before making conclusions.

2. Analyze the code for:
   - Single Responsibility Principle
   - Open/Closed Principle
   - Liskov Substitution Principle
   - Interface Segregation Principle
   - Dependency Inversion Principle

3. For every violation report:
   - exact file
   - exact class
   - concrete code evidence
   - why it violates the principle
   - proposed refactoring
   - why the proposed solution is appropriate
   - possible risks

4. Do not modify files immediately.

5. Produce an ordered refactoring plan first.

6. Avoid overengineering.

7. Preserve intended application behavior.

8. Wait for user approval before applying major modifications.

9. Apply approved refactoring incrementally.

10. Run tests or executable examples after every major change.

11. If unsure about a violation or behavior, report the uncertainty instead of guessing.