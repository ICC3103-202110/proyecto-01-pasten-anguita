class Card:

    #constantes


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
        return self.__name_card = value
            

    #metodos