# type: ignore
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    version="0.0.2",
    name="openghg_defs",
    author="Gareth Jones",
    author_email="g.m.jones@bristol.ac.uk",
    description="OpenGHG supplementary metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openghg/openghg_defs",
    packages=setuptools.find_packages(include=["openghg_defs"]),
    package_data={"openghg_defs": ["data/*", "data/domain/*", "py.typed"]},
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.8",
)
