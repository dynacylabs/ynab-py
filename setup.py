from setuptools import setup, find_packages

setup(
    name="ynab-py",
    version="1.0.0",
    description="A Python client for the You Need A Budget (YNAB) API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Austin Conn",
    author_email="austinc@dynacylabs.com",
    url="https://github.com/dynacylabs/ynab-py",
    packages=find_packages(),
    install_requires=[
        "requests",
        "python-dateutil",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
