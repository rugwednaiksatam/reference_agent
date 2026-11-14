# Contributing to toolbox

Thank you for contributing. This file tells you exactly what a mergeable
contribution looks like, so you do not have to guess.

## What belongs here

A helper that is **small**, **pure** and **generally useful**:

- takes arguments, returns a value, touches nothing else
- uses the standard library only
- would be useful to a team that has never seen your project

## What does not

- Anything needing a network, a file path, an API key or a model
- Anything that only makes sense inside one team's project
- Anything already in the standard library. `str.upper()` is not a contribution

## The process

1. **Claim an issue first.** Comment on it so two teams do not write the same
   helper. If there is no issue for your idea, open one and say what you plan.
2. **Fork** this repository and branch: `add/<module-name>`.
3. **Add one module** at `toolbox/<name>.py` and its tests at
   `tests/test_<name>.py`.
4. **Run the tests**: `python -m pytest tests/ -q`. All of them, not just yours.
5. **Open a pull request** describing what the helper does and why it is
   useful to somebody else.

## What a reviewer will check

- [ ] Every public function has a docstring saying what it returns
- [ ] At least three tests: the normal case, an edge case, and a bad input
- [ ] Bad input raises a clear error rather than returning something wrong
- [ ] No imports outside the standard library
- [ ] The whole suite passes, not only the new tests

## Style

Four-space indent, `snake_case`, lines under 88 characters. Match
`toolbox/text.py`; it is the reference.

## Review

Two approvals merge a pull request. Review somebody else's before you ask for
yours — a repository where everyone contributes and nobody reviews stops
working by Wednesday.
