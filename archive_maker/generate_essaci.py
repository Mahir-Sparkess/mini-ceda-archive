import os
import subprocess as sp


filepaths = [
    '/neodc/esacci/sst/data/lt/Analysis/L4/v01.1/1991/09/01/19910901120000-ESACCI-L4_GHRSST-SSTdepth-OSTIA-GLOB_LT-v02.0-fv01.1.nc'
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

    var_id = 'analysed_sst'
    lat_selector = '-d lat,,,10'
    lon_selector = '-d lon,,,10'
    time_selector = '-d time,,,1'

    cmd = f"ncks {lat_selector} {lon_selector} {time_selector} --variable {var_id} {filepath} {output_path}"

    print(f"[INFO] Running: {cmd}")
    sp.call(cmd, shell=True)

    print(f"[INFO] OUTPUT: {output_path}")


if __name__ == '__main__':
    for filepath in filepaths:
        create_subset_file(filepath)
