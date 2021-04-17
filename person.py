class Person:

    #constantes


    #constructor
    def __init__(
        self, name_person, coins_game, live_game
    ):
        self.__name_person = name_person
        self.__coins_game = coins_game
        self.__live_game = live_game

    #getter y setters

    @property
    def name_person(self):
        return self.__name_person

    @name_person.setter
    def name_person(self, value):
         self.__name_person = value
         return self.__name_person

    @property
    def coins_game(self):
        return self.__coins_game

    @coins_game.setter
    def coins_game(self, value):
         self.__coins_game = value
         return self.__coins_game
    
    @property
    def live_game(self):
        return self.__live_game

    @live_game.setter
    def live_game(self, value):
         self.__live_game = value
         return self.__live_game