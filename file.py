from enum import Enum

class File:
    def __init__(self, _name, _type):
        self.name = _name
        self.type = _type

    def __str__(self):
        return f"{self.name+self.type}"
