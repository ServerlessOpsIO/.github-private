---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## General Instructions

- Prioritize readability and clarity.
- Explain algorithms and key design decisions in comments.
- Handle edge cases and exceptions clearly.
- Note the purpose of external libraries in comments.
- Use consistent, idiomatic naming and code style.
- Respect existing architecture and patterns before creating new abstractions.
- Prefer explicit, readable solutions over clever shortcuts.
- Document tradeoffs when intent is not obvious.
- Reuse existing project scripts for lint, format, and tests unless asked otherwise.
- Follow repository folder conventions for modules, tests, and shared code.

## Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 96 characters.
- Use 2 blank lines to separate functions, classes, and code blocks where appropriate.

## Code

- Use descriptive function names and type hints.
- Break complex functions into smaller ones.


## Tools

- Use `black` for code formatting
- Use `flake8` for linting.
- Use `mypy` for static type checking.
- Use `pytest` for testing.
- Use `pipenv` for dependency management.

## Testing and Edge Cases

- Always write unit tests for critical code paths and edge cases.
- Test for empty inputs, invalid types, and large datasets.
- Add/update unit tests for behavior changes and edge cases.
- Add integration tests when behavior crosses service or IO boundaries.
- Add comments explaining the purpose of each test and any special edge cases.

## Dependency Management & Virtual Environments

- Track dependencies in `Pipfile` and commit both `Pipfile` and `Pipfile.lock` to version control.
- When adding dependencies, update both files with `pipenv`, preferring the latest compatible versions unless specific compatibility issues require otherwise.

## Security

- Validate and sanitize all external inputs.
- Never hardcode secrets; use secure configuration sources.
- Use parameterized queries for database access.
- Avoid dynamic code execution (eval/exec) on untrusted input.
- Prefer vetted crypto libraries and secure defaults.

## Documentation

- Use PEP 257-style docstrings for all public functions and classes.
- Docstrings should describe the purpose, parameters (with types), return value (with type), and exceptions.
- Place docstrings immediately after the `def` or `class` line.
- Use comments only to clarify complex logic or important decisions; avoid restating what the code does.

### Documentation Example

```python
import math

def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle given the radius.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle, calculated as π * radius^2.
    """
    return math.pi * radius ** 2
```
