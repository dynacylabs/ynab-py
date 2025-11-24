"""
YNAB Python Client Setup
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README
readme_file = Path(__file__).parent / "README.md"
if readme_file.exists():
    long_description = readme_file.read_text(encoding='utf-8')
else:
    long_description = "A Python client for the You Need A Budget (YNAB) API"

setup(
    name="ynab-py",
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    author="Austin Conn",
    author_email="austinc@dynacylabs.com",
    description="A Python client for the You Need A Budget (YNAB) API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dynacylabs/ynab-py",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "requests>=2.28.0",
        "python-dateutil>=2.8.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "responses>=0.22.0",
            "coverage>=7.0.0",
            "black>=22.0.0",
            "ruff>=0.1.0",
            "mypy>=0.950",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "responses>=0.22.0",
            "coverage>=7.0.0",
        ],
    },
)
