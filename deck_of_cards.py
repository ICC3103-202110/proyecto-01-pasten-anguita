class Deck_of_cards:


    #constantes

    #constructor
    def __init__(
        self, number_cards
    ):
        self.__number_card = number_card
    #getter y setters

    @property
    def number_card(self):
        return self.__number_card

    @number_card.setter
    def number_card(self, value):
         self.__number_card = value
         return self.__number_card
            

    #metodos
