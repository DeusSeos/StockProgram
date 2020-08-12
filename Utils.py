import os
import re
from screeninfo import get_monitors


def file_exists(filename) -> bool:
    return os.path.isfile(filename)


def valid_file_name(filename) -> bool:
    x = re.search('.+\..+', filename)
    if x:
        return True
    else:
        return False


def data_convert(stock) -> dict:
    data = {"Time": [], "Price": []}
    for k, v in stock.get_list().items():
        data["Time"].append(k)
        data["Price"].append(v)
    return data  # this will return a format that can be graphed easily using matlib


def getResolution() -> str:
    width = 100000
    height = 100000
    for m in get_monitors():
        if width > int(m.width):
            width = int(m.width)
        if height > int(m.height):
            height = int(m.height)
    return f"{str(width)}x{str(height)}"
