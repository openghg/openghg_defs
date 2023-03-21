from openghg_defs import get_datapath, get_domain_path

def test_get_datapath():
    site_info_fpath = get_datapath(filename="site_info.json")

    assert site_info_fpath.parts[-2:] == ('data', 'site_info.json')
    assert site_info_fpath.exists()

def test_get_domain_path():
    eastasia_lat_fpath = get_domain_path(filename="EASTASIA_latitude.dat")

    assert eastasia_lat_fpath.parts[-3:] ==  ('data', 'domain', 'EASTASIA_latitude.dat')
    assert eastasia_lat_fpath.exists()