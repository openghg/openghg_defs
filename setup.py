import setuptools
import toml

with open("pyproject.toml") as f:
    data = toml.load(f)

setuptools.setup(version=data["project"]["version"])