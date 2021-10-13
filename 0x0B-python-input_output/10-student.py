#!/usr/bin/python3
"""class student that defines a student"""



class student:
    """represent a student"""

    def __init__(self, first_name, last_name, age):
        """inicializes a new student
        arg:
        first_name: the firs name of the student
        last_name: the last name of the student
        age: the ague of the student"""


        self.first_name =first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """gets a directionary representation of the student"""
        return self.__dict__
