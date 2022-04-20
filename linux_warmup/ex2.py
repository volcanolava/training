import os.path
import re
import sys

PROC_PATH = "/proc"
FDS_PATH = "fd"
FDS_INFO_PATH = "fdinfo"


def get_filename_by_fd(fd_full_path):
    return os.path.basename(os.readlink(fd_full_path))


def get_pids():
    pids = []
    procs = os.listdir(PROC_PATH)
    for pid in procs:
        if not pid.isnumeric():
            continue
        pids.append(pid)

    return pids


def get_proc_fds(pid):
    return os.listdir(os.path.join(PROC_PATH, pid, FDS_PATH))


def print_pid_file_data(fd, pid):
    print(f"PID: {pid}\nattributes:\n")
    file_attributes = open(os.path.join(PROC_PATH, pid, FDS_INFO_PATH, fd)).read()
    print(file_attributes)


def find_procs_that_opened_file(needle):
    print(f"Found the following processes that opened the file {needle}:\n")
    for pid in get_pids():
        try:
            for fd in get_proc_fds(pid):
                file_name = get_filename_by_fd(os.path.join(PROC_PATH, pid, FDS_PATH, fd))
                if file_name != needle:
                    continue
                print_pid_file_data(fd, pid)
                break
        except OSError as e:
            continue


def main(args):
    if len(sys.argv) < 2:
        print("Usage: python ex2.py [file_name]")
        return

    file_name = sys.argv[1]
    find_procs_that_opened_file(file_name)


if __name__ == '__main__':
    main(None)
