import os


def get_file_folder(file):
    return os.path.dirname(os.path.abspath(file))

def get_full_path(file, relative_path):
    return os.path.join(get_file_folder(file), relative_path)
