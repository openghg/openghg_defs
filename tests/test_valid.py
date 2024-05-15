import json
from openghg_defs import site_info_file, species_info_file, domain_info_file


# NOTE - these tests should be expanded to check all
# data matches a simple schema for site info etc
def test_site_info_valid():
    site_info = json.loads(site_info_file.read_text())
    assert site_info


def test_species_info_valid():
    species_info = json.loads(species_info_file.read_text())
    assert species_info


def test_domain_info_valid():
    domain_info = json.loads(domain_info_file.read_text())
    assert domain_info
