from os.path import dirname, join, abspath

MAIN_DIRECTORY = dirname(dirname(dirname(abspath(__file__))))


def get_full_path(*path):
    return join(MAIN_DIRECTORY, *path)
