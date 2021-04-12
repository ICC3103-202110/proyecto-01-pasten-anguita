class Card:

    #constantes
    List_h = []


    #constructor
    def __init__(
        self, name_card
    ):
        self.__name_card = name_card
    #getter y setters

    @property
    def name_card(self):
        return self.__name_card

    @name_card.setter
    def name_card(self, value):
         self.__name_card = value
         return self.__name_card
            

    #metodos



