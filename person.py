class Person:

    #constantes


    #constructor
    def __init__(
        self, name_person
    ):
        self.__name_person = name_person

    #getter y setters

    @property
    def name_person(self):
        return self.__name_person

    @name_person.setter
    def name_person(self, value):
         self.__name_person = value
         return self.__name_person