import os
import subprocess as sp


filepaths = {
    '/neodc/baci_ssv/data/v1.0/regional_sites/13_europe/optical/rho_h18v04_2015_7day.nc': {
        'time': {
            'day': 49
        }
    },
    '/neodc/baci_ssv/data/v1.0/regional_sites/13_europe/lst/lst_h18v04_2015_7day.nc': {
        'time': {
            'time': 53
        },
    },
    '/neodc/baci_ssv/data/v1.0/regional_sites/13_europe/sar/sentinel-1_descending_h18v04_2015_7day_vv.nc': {
        'time': {
            'date': 53
        }
    },
    '/neodc/baci_ssv/data/v1.0/regional_sites/13_europe/sar/sentinel-1_ascending_h18v04_2015_7day_vv.nc': {
        'time': {
            'date': 53
        }
    }
}

mini_archive = 'archive'


def create_dir(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)


def create_time_selector(time: dict):
    return f"-d {list(time.keys())[0]},,,{list(time.values())[0]}"


def create_subset_file(filepath, variables: dict):

    print(f"[INFO] Creating subset file: {filepath}")

    path, filename = os.path.split(filepath)
    mini_dir = os.path.join(mini_archive, path.lstrip('/'))
    output_path = os.path.join(mini_dir, filename)

    create_dir(mini_dir)

    # var_id = path.split('/')[-1]
    lat_selector = '-d x,,,10'
    lon_selector = '-d y,,,10'
    time_selector = create_time_selector(variables.get('time'))

    cmd = f"ncks {lat_selector} {lon_selector} {time_selector} {filepath} {output_path}"

    print(f"[INFO] Running: {cmd}")
    sp.call(cmd, shell=True)

    print(f"[INFO] OUTPUT: {output_path}")


if __name__ == '__main__':
    for filepath, variables in filepaths.items():
        create_subset_file(filepath, variables)
