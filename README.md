# openghg_defs

This repository contains the supplementary information / metadata around site, species and domain details. This is used within the OpenGHG project.

## Installation

Note that `openghg_defs` should be installed in the same virtual environment as OpenGHG.

### Editable install

If you feel like you'll want to make changes to the metadata stored you should go for an editable install of the git repository. This will help ensure you always have the latest development changes we make to the repository. It also
means that you can make changes to your local copy of the metadata and see the results straight away in your
OpenGHG workflow.

First, clone the repository

```console
git clone https://github.com/openghg/openghg_defs.git
```

Next, move into the repository and use pip to create an editable install using the `-e` flag.

> **_NOTE:_** If you're using OpenGHG, please install `openghg_defs` in the [same virtual environment](https://docs.openghg.org/install.html#id1).

```console
cd openghg_defs
pip install -e .
```

This will create a symbolic link between the folder and your Python environment, meaning any changes you make to
the files in the repository folder will be accessible to OpenGHG.

### Install from PyPI

If you don't think you'll need to make any changes to the metadata, you can install `openghg_defs` from PyPI using `pip`:

```console
pip install openghg-defs
```

### Install from conda

You can also install `openghg_defs` from our `conda` channel:

```console
pip install -c openghg openghg-defs
```

## Usage

The path to the overall data path and primary definition JSON files are accessible using:

```python
import openghg_defs

species_info_file = openghg_defs.species_info_file
site_info_file = openghg_defs.site_info_file
domain_info_file = openghg_defs.domain_info_file
```

## Development

### Updating information

We invite users to update the information we have stored. If you find a mistake in the data or want to add something, please
[open an issue](https://github.com/openghg/supplementary_data/issues/new) and fill out the template that matches your
problem. You're also welcome to submit a pull-request with your fix.

For the recommended development process please see the [OpenGHG documentation](https://docs.openghg.org/development/python_devel.html)

### Run the tests

After making changes to the package please ensure you've added a test if adding new functionality and run the tests making sure they all pass.

```console
pytest -v tests/
```

### Release

The package is released using GitHub actions and pushed to conda and PyPI.

#### 1. Update the CHANGELOG

- Update the changelog to add the header for the new version and add the date.
- Update the Unreleased header to match the version you're releasing and `...HEAD`.

#### 2. Update `pyproject.toml`

For a new release the package version must be updated in the `pyproject.toml` file. Try and follow the [Semantic Versioning](https://semver.org/) method.

#### 3. Tag the commit

Now tag the commit. First we create the tag and add a message (remember to insert correct version numbers here).

```console
git tag -a x.x.x -m "openghg_defs release vx.x.x"
```

Next push the tag. This will trigger the automated release by GitHub Actions.

```console
git push origin x.x.x
```

#### 4. Check GitHub Actions runners

Check the GitHub Actions [runners](https://github.com/openghg/openghg_defs/actions) to ensure the tests have
all passed and the build for conda and PyPI has run successfully.
