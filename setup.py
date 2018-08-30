import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gaffer",
    version="0.1",
    author="cybermaggedon",
    author_email="cybermaggedon@gmail.com",
    description="Python Gaffer API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cybermaggedon/pygaffer",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
