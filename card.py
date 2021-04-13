import random

class Card:

    #constantes
    LIST_TYPE_CARDS = []
    LIST_RANDOM_CARDS = []
    LIST_RANDOM_NUMBERS = []


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
    def deck_cards(self):
        if self.__name_card == "Deck":
                self.LIST_TYPE_CARDS = ["Duque","Duque","Duque","Asesino","Asesino","Asesino",
                     "Capitán","Capitán","Capitán","Embajador","Embajador","Embajador",
                     "Condesa","Condesa","Condesa"]
                
    def deck_random_cards(self):
        if self.__name_card == "Deck":
            contador = 0
            while True:
                i = random.randint(0,len(self.LIST_TYPE_CARDS)-1)
                if i not in self.LIST_RANDOM_NUMBERS:
                    self.LIST_RANDOM_CARDS.append(self.LIST_TYPE_CARDS[i])   
                    self.LIST_RANDOM_NUMBERS.append(i)
                    contador +=1
                if contador ==15:
                    break
            print("the cards were randomly shuffled")
            return self.LIST_RANDOM_CARDS
                
            




