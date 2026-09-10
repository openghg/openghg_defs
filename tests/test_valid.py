from importlib.resources import files
from pathlib import Path
import json
import sys

import pytest

from openghg_defs import site_info_file, species_info_file, domain_info_file

if sys.version_info < (3,11):
    from importlib.abc import Traversable
else:
    from importlib.resources.abc import Traversable

@pytest.fixture
def data_path() -> Traversable:
    return files("openghg_defs.data")

# NOTE - these tests should be expanded to check all
# data matches a simple schema for site info etc
def test_site_info_valid():
    """Is site_info.json properly imported using `site_info_file`.

    This is how the package was operated prior to modifying it to use
    importlib. If this test passes, the previous interface still works as
    expected.
    """
    with site_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/site_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_species_info_valid():
    """Is species_info.json properly imported using `species_info_file`.

    This is how the package was operated prior to modifying it to use
    importlib. If this test passes, the previous interface still works as
    expected.
    """
    with species_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/species_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_domain_info_valid():
    """Is domain_info.json properly imported using `domain_info_file`.

    This is how the package was operated prior to modifying it to use
    importlib. If this test passes, the previous interface still works as
    expected.
    """
    with domain_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/domain_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_importlib_interface_site_info(data_path: Traversable):
    """Test if the importlib interface works for site_info."""
    with data_path.joinpath("site_info.json").open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/site_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_importlib_interface_species_info(data_path: Traversable):
    """Test if the importlib interface works for species_info."""
    with data_path.joinpath("species_info.json").open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/species_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json



def test_importlib_interface_domain_info(data_path: Traversable):
    """Test if the importlib interface works for domain_info."""
    with data_path.joinpath("domain_info.json").open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/domain_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


