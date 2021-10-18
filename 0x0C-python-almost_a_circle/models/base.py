class Base:

    """ clase Base """
    __nb_objects = 0

    def __init__(self, id=None):

        """constructor"""

        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
