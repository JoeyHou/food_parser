from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="notebookc",
    version="0.1",
    author="Joey Hou",
    author_email="z9hou@ucsd.edu",
    description="A package to parse food logging texts.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/JoeyHou/food_parser/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)