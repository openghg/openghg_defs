# openghg_defs

This repository contains the supplementary information / metadata used by the OpenGHG project.

## Installation

We recommend you install `openghg_defs` in the same virtual environment as OpenGHG.

To install `openghg_defs` using `pip` run

```bash
pip install openghg_defs
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

## Deprecated functionality

Version 0.0.1 of `openghg_defs` exposed paths to the JSON files storing the metadata. These are now deprecated and will be removed in a future version.

## Creating a release

Using GitHub actions it's easy to create a new release of the package. Submit a PR to the `main` branch
and make sure all checks are passing before merging. Ensure the PR has been reviewed by at least one other person.
Merge the PR to `main` and then run the steps below. Making **sure** you update the version number, following [semver](https://semver.org/) for the numbering. Replace x.x.x with the correct version number in the example below.

```bash
git checkout main
git pull
git tag -a x.x.x -m "openghg_defs release vx.x.x" && git push origin x.x.x
```

Then check the [GitHub actions page](https://github.com/openghg/supplementary_data/actions) and make sure it's running, you should see the tag you've given the release in blue. Give it time to complete and then check the [PyPI page](https://pypi.org/project/openghg-defs/).
