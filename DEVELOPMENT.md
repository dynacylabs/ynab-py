# Development Guide

This guide covers the development workflow, testing, and release process for ynab-py.

## Table of Contents

- [Development Setup](#development-setup)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Code Coverage](#code-coverage)
- [Development Workflow](#development-workflow)
- [Release Process](#release-process)
- [Continuous Integration](#continuous-integration)
- [Debugging](#debugging)

## Development Setup

### Prerequisites

- Python 3.8+
- Git
- pip
- Virtual environment tool (venv, virtualenv, or conda)
- YNAB account and API token

### Initial Setup

1. **Clone the Repository**

```bash
git clone https://github.com/dynacylabs/ynab-py.git
cd ynab-py
```

2. **Create Virtual Environment**

```bash
# Using venv (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Using conda
conda create -n ynab-py python=3.11
conda activate ynab-py
```

3. **Install Development Dependencies**

```bash
# Install package in editable mode
pip install -e .

# Install all development dependencies
pip install -r requirements.txt
```

4. **Verify Installation**

```bash
# Run tests
./run_tests.sh unit

# Check imports
python -c "from ynab_py import YnabPy; print('Success!')"
```

### IDE Setup

#### VS Code

Recommended extensions:
- Python (Microsoft)
- Pylance
- Python Test Explorer
- Coverage Gutters
- GitLens

Recommended settings (`.vscode/settings.json`):

```json
{
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "black",
    "python.analysis.typeCheckingMode": "basic",
    "editor.formatOnSave": true,
    "editor.rulers": [100]
}
```

#### PyCharm

1. Mark `ynab_py/` as Sources Root
2. Enable pytest as test runner
3. Configure Python 3.8+ interpreter
4. Enable type checking
5. Set Black as code formatter

## Project Structure

```
ynab-py/
├── ynab_py/                # Main package
│   ├── __init__.py        # Package initialization & exports
│   ├── api.py             # API wrapper functions
│   ├── constants.py       # Constants and configuration
│   ├── endpoints.py       # API endpoint definitions
│   ├── enums.py           # Enumerations
│   ├── pynab.py           # Core client
│   ├── schemas.py         # Data models
│   ├── utils.py           # Utility functions
│   └── ynab_py.py         # Main client class
├── tests/                  # Test suite
│   ├── __init__.py        # Test package initialization
│   └── conftest.py        # Shared fixtures and configuration
├── .github/                # GitHub configuration
│   └── workflows/         # CI/CD workflows
│       ├── tests.yml      # Test automation
│       ├── publish-to-pypi.yml  # PyPI publishing
│       ├── security.yml   # Security scanning
│       └── dependency-updates.yml # Dependency checks
├── docs/                   # Documentation
├── .gitignore             # Git ignore patterns
├── LICENSE.md             # MIT License
├── MANIFEST.in            # Package manifest
├── README.md              # Main documentation
├── INSTALL.md             # Installation guide
├── USAGE.md               # Usage guide
├── CONTRIBUTING.md        # Contribution guidelines
├── DEVELOPMENT.md         # This file
├── pyproject.toml         # Project metadata and config
├── setup.py               # Setup script
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Development dependencies
└── run_tests.sh           # Test runner script
```

## Testing

### Testing Modes

The test suite supports two modes of operation:

- **Mock Mode** (default): Uses mocked API responses for fast, offline testing
- **Live Mode**: Makes actual API calls to the YNAB API (requires valid API token)

#### Mock Mode (Default)

Mock mode runs without requiring API credentials. All API responses are mocked using the `responses` library.

```bash
# Run all tests in mock mode (default)
./run_tests.sh

# Or directly with pytest
pytest tests/
```

#### Live API Mode

Live API mode makes real requests to the YNAB API for integration testing.

```bash
# Set your API token
export YNAB_API_TOKEN="your-token-here"

# Set test mode to live
export YNAB_TEST_MODE="live"

# Run tests
./run_tests.sh
```

### Running Tests

Use the provided test runner script:

```bash
# Run all tests
./run_tests.sh

# Run only unit tests (fast)
./run_tests.sh unit

# Run integration tests
./run_tests.sh integration

# Run with coverage report
./run_tests.sh coverage

# Run specific test file
./run_tests.sh tests/test_api.py

# Run specific test
./run_tests.sh tests/test_api.py::TestYnabPy::test_initialization
```

Or use pytest directly:

```bash
# All tests
pytest

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Run tests matching pattern
pytest -k "test_budget"

# Run tests with marker
pytest -m unit
pytest -m integration
pytest -m slow
```

### Writing Tests

Follow these guidelines:

1. **Location**: Place tests in `tests/` directory
2. **Naming**: Name test files `test_*.py`
3. **Structure**: Group related tests in classes
4. **Markers**: Use pytest markers (`@pytest.mark.unit`, etc.)
5. **Fixtures**: Use fixtures from `conftest.py`

Example test structure:

```python
import pytest
from ynab_py import YnabPy

@pytest.mark.unit
class TestYnabPy:
    """Tests for the YnabPy client."""
    
    def test_initialization(self, api_key):
        """Test client initialization."""
        client = YnabPy(bearer=api_key)
        assert client.bearer == api_key
    
    def test_get_budgets(self, responses, api_key):
        """Test getting budgets list."""
        responses.add(
            responses.GET,
            "https://api.ynab.com/v1/budgets",
            json={"data": {"budgets": []}},
            status=200
        )
        client = YnabPy(bearer=api_key)
        budgets = client.budgets
        assert isinstance(budgets, dict)
```

### Test Markers

Available markers (defined in `pytest.ini`):

- `@pytest.mark.unit`: Unit tests (fast, mocked)
- `@pytest.mark.integration`: Integration tests (may hit YNAB API)
- `@pytest.mark.slow`: Slow-running tests

Usage:

```python
@pytest.mark.unit
def test_fast_operation():
    pass

@pytest.mark.integration
@pytest.mark.slow
def test_api_integration():
    pass
```

Run specific markers:

```bash
pytest -m unit           # Only unit tests
pytest -m "not slow"     # Exclude slow tests
pytest -m "unit and not slow"  # Unit tests, excluding slow
```

## Code Coverage

### Measuring Coverage

```bash
# Generate coverage report
./run_tests.sh coverage

# View in terminal
coverage report

# Generate HTML report
coverage html
# Open htmlcov/index.html in browser

# Generate XML report (for CI)
coverage xml
```

### Coverage Goals

- **Overall**: 95%+ coverage
- **New Code**: 100% coverage
- **Critical Paths**: 100% coverage

### Current Coverage Status

The test suite currently achieves **90%+ overall coverage** with comprehensive testing of:

- ✅ 100% coverage: Core modules (`__init__.py`, `cache.py`, `constants.py`, `enums.py`, `exceptions.py`, `rate_limiter.py`, `ynab_py.py`)
- ✅ 97%+ coverage: Utility functions (`utils.py`)
- ✅ 95%+ coverage: Main client class (`pynab.py`)
- 🔶 85%+ coverage: Data models and schemas (`schemas.py`)
- 🔶 83%+ coverage: API implementations (`api.py`)

The remaining coverage gaps are primarily in:
- Complex business logic requiring specific API responses
- Edge cases that are difficult to mock
- Defensive code that may never execute in normal operation
- Some schema validation paths

### Checking Coverage Locally

```bash
# Run tests with coverage
pytest --cov=ynab_py --cov-report=term-missing

# Fail if coverage below threshold
pytest --cov=ynab_py --cov-report=term --cov-fail-under=95
```

### Test Suite Overview

The test suite includes **400+ tests** covering:

- Core API functionality and error handling
- Caching with TTL and LRU eviction
- Rate limiting implementation
- Data model validation
- URL construction and query parameters
- HTTP utilities and conversions
- Custom exception hierarchy
- Mock and live API testing modes

All tests use proper isolation with the `responses` library for mocking HTTP requests, ensuring fast and reliable execution without external dependencies.

## Development Workflow

### Daily Development

1. **Pull Latest Changes**

```bash
git checkout main
git pull origin main
```

2. **Create Feature Branch**

```bash
git checkout -b feature/new-endpoint
```

3. **Make Changes**

- Edit code
- Add tests
- Update docs

4. **Run Tests**

```bash
./run_tests.sh
```

5. **Format and Lint**

```bash
# Format with Black
black ynab_py/ tests/

# Lint with Ruff
ruff check ynab_py/ tests/

# Type check with MyPy
mypy ynab_py/
```

6. **Commit Changes**

```bash
git add .
git commit -m "feat: Add new endpoint support"
```

7. **Push and Create PR**

```bash
git push origin feature/new-endpoint
# Then create PR on GitHub
```

### Code Quality Tools

#### Black (Code Formatting)

```bash
# Format all code
black ynab_py/ tests/

# Check formatting without changing
black --check ynab_py/ tests/

# Format specific file
black ynab_py/api.py
```

Configuration in `pyproject.toml`:
```toml
[tool.black]
line-length = 100
target-version = ['py38', 'py39', 'py310', 'py311', 'py312']
```

#### Ruff (Linting)

```bash
# Lint all code
ruff check ynab_py/ tests/

# Auto-fix issues
ruff check --fix ynab_py/ tests/

# Lint specific file
ruff check ynab_py/api.py
```

#### MyPy (Type Checking)

```bash
# Type check package
mypy ynab_py/

# Strict mode
mypy --strict ynab_py/

# Check specific file
mypy ynab_py/api.py
```

## Release Process

### Version Numbering

We use [Semantic Versioning](https://semver.org/):

- **MAJOR**: Incompatible API changes
- **MINOR**: New functionality, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Creating a Release

1. **Update Version**

Version is managed by `setuptools_scm` based on git tags.

2. **Create and Push Tag**

```bash
# Create annotated tag
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tag
git push origin v1.0.0
```

3. **Create GitHub Release**

- Go to GitHub Releases
- Click "Draft a new release"
- Select the tag
- Fill in release notes
- Publish release

4. **Automated Publishing**

GitHub Actions will automatically:
- Run tests
- Build distribution packages
- Publish to PyPI (if configured)

### Manual Publishing to PyPI

If needed, publish manually:

```bash
# Install build tools
pip install build twine

# Build distribution
python -m build

# Upload to TestPyPI (for testing)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## Continuous Integration

### GitHub Actions Workflows

#### Tests Workflow (`.github/workflows/tests.yml`)

Runs on:
- Push to main
- Pull requests
- Daily schedule (2am UTC)

Actions:
- Test on Python 3.8, 3.9, 3.10, 3.11, 3.12
- Run linting and type checking
- Generate coverage reports
- Upload to Codecov

#### Security Workflow (`.github/workflows/security.yml`)

Runs weekly and on pushes.

Scans:
- Dependency vulnerabilities (Safety)
- Code security issues (Bandit)
- Secret detection (TruffleHog)
- CodeQL analysis

#### Publish Workflow (`.github/workflows/publish-to-pypi.yml`)

Triggers on GitHub releases.

Actions:
- Build distribution packages
- Publish to PyPI using trusted publishing

### Local CI Simulation

Run the same checks locally:

```bash
# Run all tests like CI
pytest -v --cov=ynab_py --cov-report=term-missing

# Run linting
black --check ynab_py/ tests/
ruff check ynab_py/ tests/
mypy ynab_py/

# Security scan
pip install safety bandit
safety check
bandit -r ynab_py/
```

## Debugging

### Using pdb

```python
# Add breakpoint
import pdb; pdb.set_trace()

# Python 3.7+ breakpoint()
breakpoint()
```

### Using pytest debugger

```bash
# Drop into debugger on failure
pytest --pdb

# Drop into debugger on first failure
pytest -x --pdb
```

### Debug Logging

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

logger.debug("Debug message")
logger.info("Info message")
```

## Troubleshooting

### Common Issues

**Import errors after changes**:
```bash
pip install -e .
```

**Tests not found**:
```bash
# Ensure tests directory has __init__.py
# Check pytest.ini configuration
pytest --collect-only
```

**Coverage not working**:
```bash
# Reinstall in editable mode
pip uninstall ynab-py
pip install -e .
```

## Additional Resources

- [YNAB API Documentation](https://api.ynab.com/)
- [Python Packaging Guide](https://packaging.python.org/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## Getting Help

- Check GitHub Issues
- Read documentation
- Open a GitHub Discussion
- Contact maintainers
