import csv
import json
import os
import re


def allowed_file(file_name: str) -> bool:
    """Function gets file name and checks it's extension
    Returns bool
    """
    return "." in file_name and file_name.rsplit(".", 1)[1].lower() == "csv"


def csv_to_json(csv_file: str):
    """Function gets file name, reads it, creates list of dictionaries.
    Creates json file and writes data. Deletes old csv file
    """
    with open(csv_file, "r") as _file:
        file_reader = csv.DictReader(_file, delimiter=",")
        data = [item for item in file_reader]
        with open(csv_file[:-3] + "json", "w") as _file:
            json.dump(data, _file, indent=4)
    os.remove(csv_file)


def delete_files():
    """Function finds all json file and deletes them"""
    dir_content = os.listdir()
    expr = r"([\w]+)\.(json)"
    json_files = list(filter(lambda item: re.fullmatch(expr, item), dir_content))
    for json in json_files:
        os.remove(f"./{json}")
