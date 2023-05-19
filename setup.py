# type: ignore
import sys
import setuptools

sys.path.insert(0, ".")  # noqa
import versioneer  # noqa

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    version=versioneer.get_version(),
    name="openghg",
    author="Gareth Jones",
    author_email="g.m.jones@bristol.ac.uk",
    description="OpenGHG supplementary metadata",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/openghg/openghg_defs",
    packages=setuptools.find_packages(include=["openghg_defs"]),
    package_data={"": ["data/*", "py.typed"]},
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
