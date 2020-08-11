import os
import re


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
