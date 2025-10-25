from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mycli",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A sample CLI application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mycli",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "click>=8.1.0",
        "colorama>=0.4.6",
        "rich>=13.0.0",
        "python-dotenv>=1.0.0",
        "pyyaml>=6.0.0",
    ],
    entry_points={
        "console_scripts": [
            "mycli=cli:cli",
        ],
    },
)
