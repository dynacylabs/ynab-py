# Contributing to ynab-py

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
- [Code Quality Standards](#code-quality-standards)
- [Testing Requirements](#testing-requirements)
- [Pull Request Process](#pull-request-process)
- [Style Guide](#style-guide)
- [Documentation](#documentation)

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of background or experience level.

### Expected Behavior

- Be respectful and considerate
- Welcome newcomers and help them get started
- Focus on constructive feedback
- Be patient with questions and discussions
- Respect differing viewpoints and experiences

### Unacceptable Behavior

- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Publishing others' private information
- Any conduct inappropriate for a professional setting

## Getting Started

### Prerequisites

Before contributing, ensure you have:

- Python 3.8 or higher installed
- Git installed and configured
- A GitHub account
- A YNAB account and API token for testing
- Familiarity with pytest for testing

### First-Time Contributors

If this is your first contribution:

1. **Find an Issue**: Look for issues labeled `good first issue` or `help wanted`
2. **Ask Questions**: Don't hesitate to ask for clarification in the issue comments
3. **Small Changes**: Start with small, manageable changes
4. **Read the Docs**: Familiarize yourself with the [Usage Guide](README.md) and [Development Guide](DEVELOPMENT.md)

## Development Setup

See the [Development Guide](DEVELOPMENT.md) for detailed setup instructions.

Quick setup:

```bash
# Clone the repository
git clone https://github.com/dynacylabs/ynab-py.git
cd ynab-py

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
pip install -r requirements.txt

# Run tests to verify setup
./run_tests.sh unit
```

## How to Contribute

### Types of Contributions

We welcome various types of contributions:

- **Bug Fixes**: Fix issues reported in the issue tracker
- **New Features**: Add new functionality
- **Documentation**: Improve docs, add examples, fix typos
- **Tests**: Add test coverage, improve test quality
- **Performance**: Optimize code for better performance
- **Refactoring**: Improve code structure and readability

### Reporting Bugs

When reporting bugs, include:

- **Clear Title**: Descriptive summary of the issue
- **Description**: Detailed explanation of the problem
- **Steps to Reproduce**: Exact steps to reproduce the issue
- **Expected Behavior**: What you expected to happen
- **Actual Behavior**: What actually happened
- **Environment**: Python version, OS, package version
- **Code Sample**: Minimal code to reproduce the issue

### Suggesting Features

When suggesting new features:

1. **Check Existing Issues**: Search for similar feature requests
2. **Describe the Feature**: Clearly explain what you want
3. **Use Cases**: Provide real-world use cases
4. **Alternatives**: Mention alternatives you've considered
5. **Implementation Ideas**: Optional but helpful

### Making Changes

1. **Fork the Repository**

```bash
# Fork via GitHub UI, then clone
git clone https://github.com/YOUR-USERNAME/ynab-py.git
cd ynab-py
```

2. **Create a Branch**

```bash
# Create a descriptive branch name
git checkout -b feature/add-new-endpoint
# or
git checkout -b fix/transaction-date-parsing
```

3. **Make Your Changes**

- Write clean, readable code
- Follow the style guide
- Add or update tests
- Update documentation

4. **Test Your Changes**

```bash
# Run all tests
./run_tests.sh

# Run specific tests
pytest tests/test_api.py -v

# Check coverage
./run_tests.sh coverage
```

5. **Commit Your Changes**

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Add support for scheduled transactions endpoint"
```

Follow commit message conventions:
- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Fix bug" not "Fixes bug"
- Keep first line under 50 characters
- Reference issues: "Fix transaction parsing (#123)"

6. **Push to Your Fork**

```bash
git push origin feature/add-new-endpoint
```

7. **Open a Pull Request**

- Go to your fork on GitHub
- Click "Pull Request"
- Fill in the PR template
- Link related issues

## Code Quality Standards

### Code Style

We use several tools to maintain code quality:

```bash
# Format code with Black
black ynab_py/ tests/

# Lint with Ruff
ruff check ynab_py/ tests/

# Type check with MyPy
mypy ynab_py/
```

### Code Review Checklist

Before submitting, ensure:

- [ ] Code follows Python conventions (PEP 8)
- [ ] All tests pass
- [ ] New code has tests
- [ ] Documentation is updated
- [ ] No linting errors
- [ ] Type hints are used where appropriate
- [ ] Docstrings are added for public APIs
- [ ] Changes are backward compatible (or migration guide provided)

## Testing Requirements

### Writing Tests

- All new features must include tests
- Bug fixes should include regression tests
- Tests should be clear and well-documented
- Use descriptive test names

Example test:

```python
import pytest
from ynab_py import YnabPy

@pytest.mark.unit
class TestYnabPy:
    """Test the YnabPy client."""
    
    def test_initialization_with_api_key(self, api_key):
        """Test that client initializes with API key."""
        client = YnabPy(bearer=api_key)
        assert client.bearer == api_key
```

### Running Tests

```bash
# All tests
./run_tests.sh

# Unit tests only
./run_tests.sh unit

# With coverage
./run_tests.sh coverage

# Specific file
pytest tests/test_api.py -v
```

### Test Coverage

- Aim for 95%+ code coverage
- 100% coverage for new features
- Tests should be meaningful, not just for coverage

Check coverage:

```bash
./run_tests.sh coverage
# Then open htmlcov/index.html
```

## Pull Request Process

1. **Update Documentation**: Ensure all docs are updated
2. **Add Tests**: Include comprehensive tests
3. **Follow Template**: Fill out the PR template completely
4. **Request Review**: Tag maintainers for review
5. **Address Feedback**: Respond to review comments promptly
6. **Keep Updated**: Rebase on main if needed

### PR Title Format

- `feat: Add support for scheduled transactions`
- `fix: Resolve date parsing error in transactions`
- `docs: Update installation instructions`
- `test: Add tests for budget endpoints`
- `refactor: Simplify API error handling`

### PR Description Template

```markdown
## Description
Brief description of changes

## Motivation
Why is this change needed?

## Changes
- List of changes made
- Breaking changes (if any)

## Testing
How was this tested?

## Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] All tests pass
- [ ] No linting errors
```

## Style Guide

### Python Style

- Follow PEP 8
- Use Black for formatting (line length: 100)
- Use type hints for function signatures
- Write docstrings for public APIs (Google style)

### Example

```python
def get_budget(budget_id: str) -> dict:
    """
    Get a budget by its ID.
    
    Args:
        budget_id: The ID of the budget to retrieve.
    
    Returns:
        A dictionary containing the budget data.
    
    Raises:
        ValueError: If budget_id is empty or invalid.
    
    Example:
        >>> client = YnabPy(bearer="token")
        >>> budget = client.get_budget("budget-123")
    """
    if not budget_id:
        raise ValueError("budget_id cannot be empty")
    # Implementation...
```

## Documentation

### Updating Documentation

When making changes:

1. Update relevant `.md` files
2. Update docstrings
3. Add examples if needed
4. Update README if API changes

### Documentation Standards

- Use clear, simple language
- Include code examples
- Keep examples up to date
- Use proper Markdown formatting

## Questions?

If you have questions about contributing:

1. Check existing issues and discussions
2. Read the documentation
3. Open a GitHub issue for questions
4. Contact maintainers

Thank you for contributing! 🎉
