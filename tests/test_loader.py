from openghg_defs import load_domain_info, load_internal_json, load_site_info, load_species_info


def test_loading_site_info():
    site_info = load_site_info()

    assert site_info["WAO"] == {
        "ICOS": {
            "height": ["21m"],
            "height_name": ["20magl"],
            "height_station_masl": 10.0,
            "latitude": 52.95042,
            "long_name": "Weybourne Observatory, UK",
            "longitude": 1.12194,
        },
        "UCAM": {
            "height": ["21m"],
            "height_name": ["20magl"],
            "height_station_masl": 10.0,
            "latitude": 52.95042,
            "long_name": "Weybourne Observatory, UK",
            "longitude": 1.12194,
        },
        "UEA": {
            "height": ["21m"],
            "height_name": ["20magl"],
            "height_station_masl": 10.0,
            "latitude": 52.95042,
            "long_name": "Weybourne Observatory, UK",
            "longitude": 1.12194,
        },
    }


def test_loading_species_info():
    species_info = load_species_info()

    assert species_info["C2F6"] == {
        "alt": ["PFC-116", "PFC116", "hexafluoroethane"],
        "group": "PFCs",
        "name": "hexafluoroethane",
        "long_name": "Hexafluoroethane",
        "mol_mass": "138.012",
        "print_string": "C$_2$F$_6$",
        "units": "ppt",
    }


def test_loading_domain_info():
    domain_info = load_domain_info()

    assert domain_info["EASTASIA"] == {
        "latitude_file": "domain/EASTASIA_latitude.dat",
        "longitude_file": "domain/EASTASIA_longitude.dat",
        "latitude_range": ["-5.183", "74.143"],
        "longitude_range": ["54.516", "191.796"],
        "latitude_increment": "0.234",
        "longitude_increment": "0.352",
        "description": "NAME domain over East Asian region",
    }


def test_load_internal_json():
    site_info = load_internal_json(filename="site_info.json")

    assert site_info["ZEP"] == {
        "AGAGE": {
            "height": ["10m"],
            "height_name": ["16magl"],
            "height_station_masl": 474.0,
            "latitude": 78.925,
            "long_name": "Zeppelin, Ny Alesund, Norway",
            "longitude": 11.92222,
        },
        "NOAA": {
            "height_station_masl": 474.0,
            "latitude": 78.9067,
            "long_name": "Ny-Alesund, Svalbard, Norway and Sweden",
            "longitude": 11.8883,
        },
    }
