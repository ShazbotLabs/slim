import os
import json


def list_projects(path: str) -> list:
    file_list = []

    for entry in os.scandir(path):
        if entry.name.endswith('.json'):
            file_list.append(entry.name)

    return file_list


def read_json_file(project_file: str) -> dict:
    with open(project_file) as f:
        project_data = json.load(f)
    return project_data
