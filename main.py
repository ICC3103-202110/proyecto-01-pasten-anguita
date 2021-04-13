from card import Card
from person import Person

def players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_desk_rest_cards, number_players):
    count = 0
    if number_players == 3:
        for i in deck.LIST_RANDOM_CARDS:
            if count == 0 or count ==1 :
                list_cards_player1.append(i)
            if count ==2 or count ==3 :
                list_cards_player2.append(i)
            if count ==4 or count ==5 :
                list_cards_player3.append(i)
            if count > 5:
                list_desk_rest_cards.append(i)
            count +=1
        return list_cards_player1 , list_cards_player1, list_cards_player3, list_desk_rest_cards


def three_players(deck,number_players):
    player1 = Person("Player1")
    player2 = Person("Player2")
    player3 = Person("Player3")
    print("Its the turn of the",player1.name_person)
    list_cards_player1 = []
    list_cards_player2 = []
    list_cards_player3 = []
    list_desk_rest_cards = []
    players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_desk_rest_cards,number_players)
    print(list_cards_player1)
    print(list_cards_player2)
    print(list_cards_player3)
    print(list_desk_rest_cards)


def four_players():
    player1 = Person("Player1")
    player2 = Person("Player2")
    player3 = Person("Player3")
    player4 = Person("Player4")
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
    print("The cards can only be seen by the player of the turn")
    if number_players == 3:
        three_players(deck,number_players)
    elif number_players ==4:
        four_players()

    

    


if __name__ == "__main__":
    main()
