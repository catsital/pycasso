from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup_requirements = [
    "wheel>=0.35.1",
]

requirements = [
    "Pillow>=7.2.0",
    "Flask==2.0.2",
]

test_requirements = [
    "flake8>=3.8.3",
    "pytest>=5.4.3",
    "blinker==1.4",
]

dev_requirements = [
    *setup_requirements,
    *test_requirements,
]

extra_requirements = {
    "setup": setup_requirements,
    "test": test_requirements,
    "all": [*requirements, *dev_requirements,],
}

setup(
    name="image-scramble",
    version="2.1.2",
    author="catsital",
    author_email="catshital@gmail.com",
    description="Split image into tiles and scramble/unscramble them with seed.",
    entry_points={"console_scripts": ["pycasso=pycasso.__main__:main"],},
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
    setup_requires=setup_requirements,
    tests_require=test_requirements,
    extras_require=extra_requirements,
    zip_safe=False
)
