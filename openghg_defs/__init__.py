from pathlib import Path

module_root = Path(__file__).resolve().parent

data_path: Path = module_root / "data"

site_info_file: Path = data_path / "site_info.json"
species_info_file: Path = data_path / "species_info.json"
domain_info_file: Path = data_path / "domain_info.json"
