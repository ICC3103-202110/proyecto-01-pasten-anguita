from card import Card
from deck_of_cards import Deck_of_cards
from person import Person



def main():
    

    card1 = Card("Duque")
    card2 = Card("Duque")
    card3 = Card("Duque")
    card4 = Card("Asesino")
    card5 = Card("Asesino")
    card6 = Card("Asesino")
    card7 = Card("Capitán")
    card8 = Card("Capitán")
    card9 = Card("Capitán")
    card10 = Card("Embajador")
    card11 = Card("Embajador")
    card12 = Card("Embajador")
    card13 = Card("Condesa")
    card14 = Card("Condesa")
    card15 = Card("Condesa")
  
    deck = Deck_of_cards(int(15))
    print(deck.LIST_TYPE_CARDS)
    deck.random_cards()
    print(len(deck.LIST_TYPE_CARDS))
    print(deck.LIST_RANDOM_CARDS)
    


    


if __name__ == "__main__":
    main()
