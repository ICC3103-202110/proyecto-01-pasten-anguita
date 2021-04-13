import random

class Deck_of_cards:


    #constantes
    LIST_TYPE_CARDS = ["Duque","Duque","Duque","Asesino","Asesino","Asesino",
                    "Capitán","Capitán","Capitán","Embajador","Embajador","Embajador",
                    "Condesa","Condesa","Condesa"]
    LIST_RANDOM_CARDS = []
    LIST_RANDOM_NUMBERS = []
    #constructor
    def __init__(
        self, number_cards
    ):
        self.__number_cards = number_cards
    #getter y setters

    @property
    def number_cards(self):
        return self.__number_cards

    @number_cards.setter
    def number_cards(self, value):
         self.__number_cards = value
         return self.__number_cards
            

    #metodos

    def random_cards(self):
        contador = 0
        while True:
            i = random.randint(0,len(self.LIST_TYPE_CARDS)-1)
            if i not in self.LIST_RANDOM_NUMBERS:
                self.LIST_RANDOM_CARDS.append(self.LIST_TYPE_CARDS[i])   
                self.LIST_RANDOM_NUMBERS.append(i)
                contador +=1
            if contador ==15:
                break
        return self.LIST_RANDOM_CARDS
        
                
    


