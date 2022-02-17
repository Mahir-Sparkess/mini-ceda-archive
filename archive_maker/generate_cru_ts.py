import os
import subprocess as sp


filepaths = [
    '/badc/cru/data/cru_ts/cru_ts_4.02/data/tmp/cru_ts4.02.1901.2017.tmp.dat.nc',
    '/badc/cru/data/cru_ts/cru_ts_4.02/data/pre/cru_ts4.02.1901.2017.pre.dat.nc'
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

    var_id = path.split('/')[-1]
    lat_selector = '-d lat,,,10'
    lon_selector = '-d lon,,,10'
    time_selector = '-d time,,,1404'

    cmd = f"ncks {lat_selector} {lon_selector} {time_selector} --variable {var_id} {filepath} {output_path}"

    print(f"[INFO] Running: {cmd}")
    sp.call(cmd, shell=True)

    print(f"[INFO] OUTPUT: {output_path}")


if __name__ == '__main__':
    for filepath in filepaths:
        create_subset_file(filepath)
