import os
import json

from typing import List, Any


def list_projects(path: str) -> List[str]:
    file_list = []

    for entry in os.scandir(path):
        if entry.name.endswith('.json'):
            file_list.append(entry.name)

    return file_list


def read_json_file(project_file: str) -> Any:
    with open(project_file) as f:
        project_data = json.load(f)
    return project_data
