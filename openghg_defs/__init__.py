import warnings as _warnings

from ._load import load_domain_info, load_internal_json, load_site_info, load_species_info
from ._paths import get_domain_path, get_datapath

_warnings.warn(
    message="Direct access to filepaths will be removed in the next release."
    + " Please start using either the loader functions or get_datapath.",
    category=DeprecationWarning,
)
del _warnings

data_path = get_datapath(filename="unused").parent
species_info_file = get_datapath(filename="species_info.json")
site_info_file = get_datapath(filename="site_info.json")
domain_info_file = get_datapath(filename="domain_info.json")
