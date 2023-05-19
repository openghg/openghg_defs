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

```console
cd openghg_defs
pip install -e .
```

This will create a symbolic link between the folder and your Python environment, meaning any changes you make to
the files in the repository folder will be accessible to OpenGHG.

### Install from PyPI

If you don't think you'll need to make any changes to the metadata, you can install `openghg_defs` from PyPI using `pip`.

```console
pip install openghg-defs
```

## Usage

The primary definition JSON files are accessible using either the loading functions

- `load_site_info` - load site information dictionary
- `load_domain_info` - load domain info dictionary
- `load_species_info` - load species info dictionary

For example

```ipython3
In [1]: import openghg_defs

In [2]: species_info = openghg_defs.load_species_info()

In [3]: species_info
Out[3]:
{'APO': {'alt': ['atmospheric_potential_oxygen'],
  'group': 'Other',
  'name': 'atmospheric_potential_oxygen',
  'long_name': 'Atmospheric Potential Oxygen',
  'mol_mass': 'None',
  'print_string': 'APO',
  'units': 'per meg'},
 'C2F6': {'alt': ['PFC-116', 'PFC116', 'hexafluoroethane'],
  ...
 ```

You can also get the path of the file directly:

```ipython3
In [1]: from openghg_defs import get_datapath
   ...:
   ...: fpath = get_datapath(filename="site_info.json")

In [2]: fpath
Out[2]: PosixPath('/home/gareth/Documents/Devel/supplementary_data/openghg_defs/data/site_info.json')
```

Currently the paths to the files are also available directly by import:

```python
import openghg_defs

species_info_file = openghg_defs.species_info_file
site_info_file = openghg_defs.site_info_file
domain_info_file = openghg_defs.domain_info_file
```

These may be removed in future versions so we recommend using the function call functionality above.

## Updating information

We invite users to update the information we have stored. If you find a mistake in the data or want to add something, please
[open an issue](https://github.com/openghg/supplementary_data/issues/new) and fill out the template that matches your
problem.

You're also welcome to submit a pull-request with your fix.