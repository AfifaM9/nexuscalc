"""Setup configuration for NexusCalc."""

from setuptools import setup, find_packages
import os
import re

# Read version from __init__.py
with open("src/nexuscalc/__init__.py", "r", encoding="utf-8") as f:
    version_match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', f.read())
    version = version_match.group(1) if version_match else "2.1.0-rc.1"

# Read README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nexuscalc",
    version=version,
    author="Light Bulb Experiments",
    author_email="lightbulb@experiments.com",
    description="🔢 A chill CLI calculator that just works",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AfifaM9/nexuscalc",
    project_urls={
        "Bug Reports": "https://github.com/AfifaM9/nexuscalc/issues",
        "Source": "https://github.com/AfifaM9/nexuscalc",
        "PyPI": "https://pypi.org/project/nexuscalc/",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "nexuscalc=nexuscalc:start_calc",
        ],
    },
    keywords="calculator, math, arithmetic, cli, interactive, terminal, python, modulo",
    license="MIT",
    platforms=["Windows", "macOS", "Linux"],
)
