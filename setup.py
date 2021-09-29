from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

requirements = ["Pillow>=7.2.0"]

setup(
    name="pycasso",
    version="1.0.0",
    author="catsital",
    author_email="catshital@gmail.com",
    description="Split image into tiles and scramble/unscramble it with seed.",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/catsital/pycasso",
    project_urls={
        "Bug Tracker": "https://github.com/catsital/pycasso/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    zip_safe=False
)
