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
                self.LIST_TYPE_CARDS = ["Duke","Duke","Duke","Assassin","Assassin","Assassin",
                     "Captain","Captain","Captain","Ambassador","Ambassador","Ambassador",
                     "Countess","Countess","Countess"]
                
    def deck_random_cards(self):
        if self.__name_card == "Deck":
            count = 0
            while True:
                i = random.randint(0,len(self.LIST_TYPE_CARDS)-1)
                if i not in self.LIST_RANDOM_NUMBERS:
                    self.LIST_RANDOM_CARDS.append(self.LIST_TYPE_CARDS[i])   
                    self.LIST_RANDOM_NUMBERS.append(i)
                    count +=1
                if count ==15:
                    break
            print("the cards were randomly shuffled")
            return self.LIST_RANDOM_CARDS
                
            




