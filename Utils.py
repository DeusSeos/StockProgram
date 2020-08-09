import os
import re


def file_exists(filename) -> bool:
    return os.path.isfile(filename)

def valid_file_name(filename) -> bool:
    x = re.search(".+\..+", filename)
    if x:
        return True
    else:
        return False
