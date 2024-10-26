from setuptools import setup, find_packages

setup(
    name="my_python_package",
    version="0.0.01",
    author="Bera",
    author_email="beraerentutkun04@gmail.com",
    description="Python toolbox library for non-coders and low-coders",
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
