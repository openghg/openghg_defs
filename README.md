# openghg_defs

This repository contains the supplementary information / metadata used by the OpenGHG project.

## Installation

Note that `openghg_defs` should be installed in the same virtual environment as OpenGHG.
There are two ways of installing `openghg_defs`, as an editable install of this git repository or via PyPI. 

### Editable install

If you feel like you'll want to make changes to the metadata stored you should go for an editable install of the git repository. This will help ensure you always have the latest development changes we make to the repository. It also
means that you can make changes to your local copy of the metadata and see the results straight away in your
OpenGHG workflow.

First, clone the repository

```console
git clone https://github.com/openghg/openghg_defs.git
```

Next, move into the repository and use pip to create an editable install using the `-e` flag.

> **_NOTE:_**  If you're using OpenGHG, please install `openghg_defs` in the [same virtual environment](https://docs.openghg.org/install.html#id1).

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

## Updating information

We invite users to update the information we have stored. If you find a mistake in the data or want to add something, please
[open an issue](https://github.com/openghg/supplementary_data/issues/new) and fill out the template that matches your
problem.

You're also welcome to submit a pull-request with your fix.