"""
File: file.py
Author: Steven "Kabbe" Karbjinsky
Description: ...

For more information, see: https://github.com/xKabbe/spark
"""
import time
from datetime import datetime
from os import stat_result
from pathlib import Path


class File:
    def __init__(self, name, extension, stats: stat_result, parent_directory):
        self.name = name
        self.extension = extension
        self.size: int = stats.st_size  # in bytes
        self.creation_time = stats.st_ctime
        self.modification_time = stats.st_mtime
        self.parent_directory = parent_directory

        self.content = []
        self.lines_of_content = 0
        self.characters_of_content = 0
        self._read_file_content()

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'extension': self.extension,
            'size': self.size,
            'creation_time': datetime.fromtimestamp(self.creation_time),
            'modification_time': datetime.fromtimestamp(self.modification_time),
            'parent_directory': self.parent_directory,
            'content': self.content,
            'lines_of_content': self.lines_of_content,
            'characters_of_content': self.characters_of_content
        }

    def _read_file_content(self):
        # path = f'{self.parent_directory}/{self.name}.{self.extension}'
        #
        # content = []
        # lines_of_content = 0
        # characters_of_content = 0
        # with open(path, 'r') as file:
        #     for line in file:
        #         content.append(line)
        #         lines_of_content += 1
        #         characters_of_content += len(line)
        #
        # self.content = content
        # self.lines_of_content = lines_of_content
        # self.characters_of_content = characters_of_content
        path = f'{self.parent_directory}/{self.name}.{self.extension}'

        with open(path, 'r') as file:
            content = [line for line in file]
            # content = '\\n'.join(file.readlines())

        self.content = content
        self.lines_of_content = len(content)
        self.characters_of_content = sum([len(line) for line in content])
