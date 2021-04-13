from card import Card
from person import Person


def three_players(card1):
    player1 = Person("Player1")
    player2 = Person("Player2")
    player3 = Person("Player1")
    print(card1.name_card)


def four_players():
    print("chao")

def main():

    deck = Card("Deck")
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

    print(deck.name_card)
    deck.deck_cards()
    print(deck.LIST_TYPE_CARDS)
    deck.deck_random_cards()
    print(deck.LIST_RANDOM_CARDS)

 

    number_players = int(input("how many players will play this game? 3 or 4 : "))
    if number_players == 3:
        three_players(card1)
    elif number_players ==4:
        four_players()

    

    


if __name__ == "__main__":
    main()
