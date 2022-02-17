import os
import subprocess as sp


filepaths = [
    '/badc/cmip6/data/CMIP6/CMIP/NCAR/CESM2/abrupt-4xCO2/r1i1p1f1/Amon/tas/gn/v20190927/tas_Amon_CESM2_abrupt-4xCO2_r1i1p1f1_gn_095001-099912.nc'
]

mini_archive = 'archive'


def create_dir(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)


def create_subset_file(filepath):

    print(f"[INFO] Creating subset file: {filepath}")

    path, filename = os.path.split(filepath)
    mini_dir = os.path.join(mini_archive, path.lstrip('/'))
    output_path = os.path.join(mini_dir, filename)

    create_dir(mini_dir)

    var_id = filename.split('_')[0]
    lat_selector = '-d lat,,,10'
    lon_selector = '-d lon,,,10'
    time_selector = '-d time,,,600'

    cmd = f"ncks {lat_selector} {lon_selector} {time_selector} --variable {var_id} {filepath} {output_path}"

    print(f"[INFO] Running: {cmd}")
    sp.call(cmd, shell=True)

    print(f"[INFO] OUTPUT: {output_path}")


if __name__ == '__main__':
    for filepath in filepaths:
        create_subset_file(filepath)
