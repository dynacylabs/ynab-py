# Installation Guide

This guide covers how to install ynab-py.

## Table of Contents

- [Requirements](#requirements)
- [Installation Methods](#installation-methods)
  - [From PyPI (Recommended)](#from-pypi-recommended)
  - [From Source](#from-source)
  - [Development Installation](#development-installation)
- [Verification](#verification)
- [Getting a YNAB API Token](#getting-a-ynab-api-token)
- [Troubleshooting](#troubleshooting)

## Requirements

- **Python**: 3.8 or higher
- **pip**: Latest version recommended
- **Dependencies**: 
  - `requests >= 2.28.0`
  - `python-dateutil >= 2.8.0`
- **YNAB Account**: Required for API access

## Installation Methods

### From PyPI (Recommended)

The easiest way to install the library is from PyPI using pip:

```bash
pip install ynab-py
```

To upgrade to the latest version:

```bash
pip install --upgrade ynab-py
```

To install a specific version:

```bash
pip install ynab-py==1.0.0
```

### From Source

To install directly from the GitHub repository:

```bash
# Clone the repository
git clone https://github.com/dynacylabs/ynab-py.git
cd ynab-py

# Install
pip install .
```

Or install directly from GitHub without cloning:

```bash
pip install git+https://github.com/dynacylabs/ynab-py.git
```

### Development Installation

For development, install in editable mode with all dependencies:

```bash
# Clone the repository
git clone https://github.com/dynacylabs/ynab-py.git
cd ynab-py

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .

# Install development dependencies
pip install -r requirements.txt
```

This allows you to make changes to the code and see them reflected immediately without reinstalling.

### Optional Dependencies

If you need development tools:

```bash
pip install ynab-py[dev]
```

This includes:
- pytest and plugins for testing
- black for code formatting
- ruff for linting
- mypy for type checking
- coverage tools

## Verification

After installation, verify it's working correctly:

### Command Line Verification

```bash
python -c "from ynab_py import YnabPy; print('Installation successful!')"
```

### Python Script Verification

Create a file `test_install.py`:

```python
from ynab_py import YnabPy

# Test basic functionality (requires API token)
# Replace 'YOUR_API_TOKEN' with your actual token
try:
    ynab = YnabPy(bearer="YOUR_API_TOKEN")
    print("✓ Installation successful!")
    print(f"✓ Connected to YNAB API")
except Exception as e:
    print(f"✗ Installation test failed: {e}")
```

Run it:

```bash
python test_install.py
```

### Run Tests

If you installed from source:

```bash
# Run the test suite
./run_tests.sh unit

# Or use pytest directly
pytest tests/ -v
```

## Getting a YNAB API Token

To use ynab-py, you need a personal access token from YNAB:

1. Go to [YNAB Account Settings](https://app.ynab.com/settings)
2. Navigate to "Developer Settings"
3. Click "New Token"
4. Give your token a name (e.g., "ynab-py")
5. Copy the generated token
6. Store it securely (you won't be able to see it again)

**Security Note**: Never commit your API token to version control or share it publicly.

### Using Environment Variables

It's recommended to store your token in an environment variable:

```bash
# Linux/macOS
export YNAB_API_TOKEN="your_token_here"

# Windows (Command Prompt)
set YNAB_API_TOKEN=your_token_here

# Windows (PowerShell)
$env:YNAB_API_TOKEN="your_token_here"
```

Then in your Python code:

```python
import os
from ynab_py import YnabPy

api_token = os.environ.get("YNAB_API_TOKEN")
ynab = YnabPy(bearer=api_token)
```

### Using a .env File

For local development, you can use a `.env` file:

```bash
# .env file
YNAB_API_TOKEN=your_token_here
```

Then use a library like `python-dotenv`:

```bash
pip install python-dotenv
```

```python
from dotenv import load_dotenv
import os
from ynab_py import YnabPy

load_dotenv()
api_token = os.environ.get("YNAB_API_TOKEN")
ynab = YnabPy(bearer=api_token)
```

## Troubleshooting

### Common Issues

#### Import Error: No module named 'ynab_py'

**Solution**: Make sure you've installed the package:
```bash
pip install ynab-py
# or for development:
pip install -e .
```

#### Permission Denied Error

**Solution**: Use `--user` flag or a virtual environment:
```bash
pip install --user ynab-py
```

Or create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install ynab-py
```

#### Old Version Installed

**Solution**: Force reinstall:
```bash
pip install --upgrade --force-reinstall ynab-py
```

#### Dependency Conflicts

**Solution**: Use a fresh virtual environment:
```bash
python -m venv fresh_env
source fresh_env/bin/activate
pip install ynab-py
```

#### API Connection Issues

**Symptoms**: Connection errors, timeout errors, or authentication failures.

**Solutions**:
1. Verify your API token is correct
2. Check your internet connection
3. Verify YNAB API status at [status.ynab.com](https://status.ynab.com)
4. Ensure you're using HTTPS (not HTTP)

#### SSL Certificate Errors

**Symptoms**: SSL verification failures.

**Solution**: Update your `certifi` package:
```bash
pip install --upgrade certifi
```

### Getting Help

If you encounter issues:

1. Check the [GitHub Issues](https://github.com/dynacylabs/ynab-py/issues) for similar problems
2. Review the [YNAB API documentation](https://api.ynab.com/)
3. Create a new issue with:
   - Your Python version (`python --version`)
   - Your pip version (`pip --version`)
   - Your operating system
   - The full error message
   - Steps to reproduce the issue

## Next Steps

- Read the [Usage Guide](USAGE.md) to learn how to use the library
- Check the [Development Guide](DEVELOPMENT.md) for contributing
- Review the [README](README.md) for quick examples
- Visit [YNAB API Documentation](https://api.ynab.com/) for API details
