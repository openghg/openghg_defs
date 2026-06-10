"""Definitions for sites, domains and species used in OpenGHG.

Examples
--------
>>> import json
>>> from openghg_defs import openghg_defs_files
>>> site_info_json = openghg_defs_files / "site_info.json"
>>> with site_info_json.open("rb") as js:
...     site_info = json.load(js)

"""
from importlib.resources import files
import sys

if sys.version_info < (3,11):
    from importlib.abc import Traversable
else:
    from importlib.resources.abc import Traversable

openghg_defs_files: Traversable = files("openghg_defs.data")
"""Base directory for OpenGHG Definition files.

This is a `Traversable` (similar to `pathlib.Path`) object that can be used
to access the other files in the package.

"""

site_info_file: Traversable = openghg_defs_files / "site_info.json"
"""Link to measurement site information relevant to OpenGHG.

This is a `Traversable` (similar to `pathlib.Path`) object that can be used
to access the file via a context manager.
"""

species_info_file: Traversable = openghg_defs_files / "species_info.json"
"""Link to atmospheric species information relevant to OpenGHG.

This is a `Traversable` (similar to `pathlib.Path`) object that can be used
to access the file via a context manager.
"""

domain_info_file: Traversable = openghg_defs_files / "domain_info.json"
"""Link to measurement domain information relevant to OpenGHG.

This is a `Traversable` (similar to `pathlib.Path`) object that can be used
to access the file via a context manager.
"""
