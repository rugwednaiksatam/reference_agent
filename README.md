# toolbox

A shared library of small, reusable helpers, written by everyone on the
course. One module per team.

Every function here is **dependency-free**, **pure**, and **tested**. If it
needs a network, a file or a model, it does not belong in this repository.

## Using it

```python
from toolbox.text import word_count, truncate

word_count("one two three")      # 3
truncate("hello world", 8)       # 'hello...'
```

## Running the tests

```bash
python -m pytest tests/ -q
```

## Contributing

Read `CONTRIBUTING.md` first. The short version:

1. Fork, branch, add **one** module under `toolbox/` and its tests under `tests/`
2. Every public function needs a docstring and at least three tests
3. Tests pass locally before you open the pull request
4. One pull request per team

`toolbox/text.py` is the worked example. Copy its shape.
