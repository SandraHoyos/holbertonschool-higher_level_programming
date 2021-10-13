#!/usr/bin/python3
"""creates a student"""


class student:
    """class that defines a student
    public attributes:
    first_name
    last_name
    age
    public method to:json()"""

    def __init__(self, first_name, last_name, age):
        """initializes the student instance
        arg:
        first_name: the first name of the student
        last_name: the last name the student
        age: the age of the student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a dictionary representation of the student"""

        return self.__dict__
