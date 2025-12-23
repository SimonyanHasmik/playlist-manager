from setuptools import setup, find_packages

setup(
    name="playlist-manager",
    version="0.1.1",
    description="A Python package for playlist management",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Hasmik Simonyan",
    author_email="your-email@example.com",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=[
        "requests"
    ],
)

