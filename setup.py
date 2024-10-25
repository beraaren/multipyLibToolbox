from setuptools import setup, find_packages

setup(
    name="my_python_package",
    version="0.1.0",
    author="Bera",
    author_email="your-email@example.com",
    description="A simple Python package example",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my_python_package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
