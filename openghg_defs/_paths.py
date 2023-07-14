from pathlib import Path


def get_domain_path(filename: str) -> Path:
    """Get the filepath of a domain file

    Args:
        filename: Name of domain file
    Returns:
        Path: Filepath
    """
    return Path(__file__).parent.resolve().joinpath("data", "domain", filename)


def get_datapath(filename: str) -> Path:
    """Return the full path to a file in the internal openghg_defs data folder

    Args:
        filename: Name of file
    Returns:
        Path: Filepath
    """
    return Path(__file__).parent.resolve().joinpath("data", filename)
