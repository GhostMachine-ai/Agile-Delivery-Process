```markdown
# Agile-Delivery-Process Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `Agile-Delivery-Process` Python repository. It covers file naming, import/export styles, commit message patterns, and testing strategies. By following these guidelines, contributors can maintain consistency and quality throughout the codebase.

## Coding Conventions

### File Naming
- Use **snake_case** for all file and module names.

**Example:**
```python
# Good
agile_process.py
delivery_utils.py

# Bad
AgileProcess.py
deliveryUtils.py
```

### Import Style
- Use **relative imports** within the package.

**Example:**
```python
# In delivery_utils.py
from .agile_process import AgileProcess
```

### Export Style
- Use **named exports** (explicitly define what is exported).

**Example:**
```python
# In agile_process.py
class AgileProcess:
    pass

__all__ = ['AgileProcess']
```

### Commit Message Patterns
- Commit messages are **freeform** and do not follow a strict template.
- Commonly, messages are concise (average 93 characters) and may use prefixes, but this is not enforced.

**Example:**
```
Add new delivery workflow for sprint planning
Fix bug in agile_process.py when handling empty tasks
```

## Workflows

_No automated or documented workflows detected in the repository._

## Testing Patterns

- **Framework:** Unknown (no specific testing framework detected).
- **Test File Pattern:** Test files follow the `*.test.*` naming convention.

**Example:**
```
test_agile_process.test.py
delivery_utils.test.py
```

- Place test files alongside the modules they test or in a dedicated test directory.
- Test functions and classes should be named clearly to indicate what they are testing.

**Example:**
```python
# In test_agile_process.test.py
def test_agile_process_initialization():
    process = AgileProcess()
    assert process is not None
```

## Commands

| Command | Purpose |
|---------|---------|
| /test   | Run all test files matching *.test.* |
```
