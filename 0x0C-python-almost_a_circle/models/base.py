#!/usr/bin/python3
"""Base class"""

import json


class Base:
    """Represents the base class
    Observation:
        The class is used to manage id attribute
        in all your future classes and to avoid duplicating
        the same code (by extension, same bugs)
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiates the id class with
        Args:
            id(int): the class id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation
        of list_dictionaries
        Args:
            list_dictionaries(list): list of dictionary
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of
        list_objs to a file
        Args:
            list_objs(): a list of instances who inherits ofBase -
            example: list of Rectangle or list of Square instances
        """
        if list_objs is None:
            with open(cls.__name__ + ".json", "w") as file:
                file.write("[]")
        else:
            list_instance = [i.to_dictionary() for i in list_objs]
            with open(cls.__name__ + ".json", "w") as file:
                file.write(cls.to_json_string(list_instance))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string
        representation json_string
        Args:
            json_string(str): a string representing a list
            of dictionaries
        """
        if json_string is None:
            return []
        if json_string == [] or not isinstance(json_string, str):
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            **dictionary(pointer): can be thought of as a
            double pointer to a dictionary
        """
        if cls.__name__ == "Rectangle":
            result = cls(32, 3)
            result.update(**dictionary)
            return result
        if cls.__name__ == "Square":
            result = cls(32)
            result.update(**dictionary)
            return result

    @classmethod
    def load_from_file(cls):
        """
        This function returns a list
        of instances
        """
        fn = cls.__name__ + ".json"
        lst = []
        try:
            with open(fn, mode="r") as myFile:
                lst = cls.from_json_string(myFile.read())
            for i, j in enumerate(lst):
                lst[i] = cls.create(**lst[i])
        except:
            pass
        return (lst)
