import os.path
import re
import sys


def print_open_files(proc_id):
    MAPPING_IND = 0
    FILE_PATH_IND = 5
    MIN_MAPPING_DATA_LEN = 6

    with open(f"/proc/{proc_id}/maps") as maps_file:
        for map_line in maps_file.readlines():
            mapping_data = map_line.split()
            if len(mapping_data) < MIN_MAPPING_DATA_LEN or not os.path.isfile(mapping_data[FILE_PATH_IND]):
                continue
            print(f"File {mapping_data[FILE_PATH_IND]} is mapped to range {mapping_data[MAPPING_IND]}")


def main(args):
    if len(sys.argv) < 2:
        print("Usage: python ex1.py [pid]")
        return

    proc_id = sys.argv[1]
    print_open_files(proc_id)


if __name__ == '__main__':
    main(None)
