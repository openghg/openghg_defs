from pathlib import Path
import json

from openghg_defs import site_info_file, species_info_file, domain_info_file


# NOTE - these tests should be expanded to check all
# data matches a simple schema for site info etc
def test_site_info_valid():
    with site_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/site_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_species_info_valid():
    with species_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/species_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json


def test_domain_info_valid():
    with domain_info_file.open("rb") as interface:
        pkg_json = json.load(interface)
    with Path("./openghg_defs/data/domain_info.json").open("rb") as local:
        local_json = json.load(local)
    assert pkg_json == local_json
