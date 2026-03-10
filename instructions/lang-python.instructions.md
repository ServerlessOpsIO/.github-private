---
description: 'Python coding conventions and guidelines'
applyTo: '**/*.py'
---

# Python Coding Conventions

## General Instructions

- Always prioritize readability and clarity.
- For algorithm-related code, include explanations of the approach used.
- Write code with good maintainability practices, including comments on why certain design decisions were made.
- Handle edge cases and write clear exception handling.
- For libraries or external dependencies, mention their usage and purpose in comments.
- Use consistent naming conventions and follow language-specific best practices.
- Write concise, efficient, and idiomatic code that is also easily understandable.

## Python Instructions

- Ensure functions have descriptive names and include type hints.
- Use the `typing` module for type annotations (e.g., `List[str]`, `Dict[str, int]`).
- Break down complex functions into smaller, more manageable functions.
- Use `TypedDict` for structured data when appropriate.
  - Use `dataclasses` for structured data when methods or default values are needed.

## Code Style and Formatting

- Follow the **PEP 8** style guide for Python.
- Maintain proper indentation (use 4 spaces for each level of indentation).
- Ensure lines do not exceed 79 characters.
- Use blank lines to separate functions, classes, and code blocks where appropriate.

## Edge Cases and Testing

- Always include test cases for critical paths of the application.
- Account for common edge cases like empty inputs, invalid data types, and large datasets.
- Include comments for edge cases and the expected behavior in those cases.
- Write unit tests for functions and document them with docstrings explaining the test cases.

## Dependency Management & Virtual Environments

- Use `pipenv` to manage dependencies and virtual environments.
- Include a `Pipfile` in the project to track dependencies and their versions.
- A `Pipfile.lock` should be generated using `pipenv` and committed to version control for consistent dependency management across different environments.
- When adding new dependencies:
  - update the `Pipfile` and regenerate the `Pipfile.lock` to ensure all dependencies are properly tracked and versioned.
  - preffer using the latest compatible version of the dependency unless there is a specific reason to use an older version (for example compatibility with other dependencies or known issues with newer versions).

## Documentation
- Provide docstrings following PEP 257 conventions.
- Docstrings should include a description of the function's purpose, its parameters (with types), return value (with type), and any exceptions that may be raised.
- Place function and class docstrings immediately after the `def` or `class` keyword.
- Write clear and concise comments within a function, sparingly and only when necessary, to explain complex logic or important details.
- Docstrings should describe what codes does while comments should explain how the code does it and why certain decisions were made. Avoid redundant comments that simply restate what the code does without adding additional context or explanation.

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
