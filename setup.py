import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="puzzle",
    version="0.0.1",
    author="Yaroslav Romanus",
    author_email="yaroslav.romanus@ucu.edu.ua",
    description="solution of puzzle game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yarkoslav/puzzle",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
