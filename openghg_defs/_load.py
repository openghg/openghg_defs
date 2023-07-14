import json
from pathlib import Path
from typing import Dict


def load_internal_json(filename: str) -> Dict:
    """Load a JSON file from the data folder.

    Returns:
        dict: Dictionary from JSON
    """
    from openghg_defs import get_datapath

    fpath = get_datapath(filename=filename)
    return json.loads(fpath.read_text())


def load_domain_info() -> Dict:
    """Load the domain info from the data folder

    Returns:
        dict: Domain info
    """
    return load_internal_json(filename="domain_info.json")


def load_site_info() -> Dict:
    """Load the site info from the data folder

    Returns:
        dict: Site info
    """
    return load_internal_json(filename="site_info.json")


def load_species_info() -> Dict:
    """Load the species info from the data folder

    Returns:
        dict: Species info
    """
    return load_internal_json(filename="species_info.json")
