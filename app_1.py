# Напишите функцию,
# которая сереализует содержимое текущей директории в json-файл.
# В файле должен храниться список словарей,
# словарь описывает элемент внутри директории:
# имя, расширение, тип.
# Если элемент - директория, то только тип и имя.

import os
import json


def serialize_directory_to_json(directory_path):
    """The function serializes the contents of the specified directory into
    JSON format and saves this JSON to a file."""
    items = []
    for item_name in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item_name)
        item_info = {'name': item_name}

        if os.path.isfile(item_path):
            item_info['type'] = 'file'
            item_info['extension'] = os.path.splitext(item_name)[1]
        elif os.path.isdir(item_path):
            item_info['type'] = 'directory'

        items.append(item_info)

    json_filename = os.path.join(directory_path, 'directory_contents.json')
    with open(json_filename, 'w') as json_file:
        json.dump(items, json_file, indent=4)
