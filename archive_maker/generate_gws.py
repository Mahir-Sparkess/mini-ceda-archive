import os
import subprocess as sp


filepaths = [
    '/gws/nopw/j04/cedaproc/public-data/uk_max_temp.txt'
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

    cmd = f"cp {filepath} {output_path}"

    print(f"[INFO] Running: {cmd}")
    sp.call(cmd, shell=True)

    print(f"[INFO] OUTPUT: {output_path}")


if __name__ == '__main__':
    for filepath in filepaths:
        create_subset_file(filepath)
