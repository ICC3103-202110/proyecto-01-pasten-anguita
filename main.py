from card import Card
from person import Person

def distribution_of_cards(list_players):
    print("hola")

def players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_desk_rest_cards, number_players):
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
    
    if number_players == 4:
        for i in deck.LIST_RANDOM_CARDS:
            if count == 0 or count ==1 :
                list_cards_player1.append(i)
            if count ==2 or count ==3 :
                list_cards_player2.append(i)
            if count ==4 or count ==5 :
                list_cards_player3.append(i)
            if count ==6 or count ==7 :
                list_cards_player4.append(i)
            if count > 7:
                list_desk_rest_cards.append(i)
            count +=1
        return list_cards_player1 , list_cards_player1, list_cards_player3,list_cards_player4 ,list_desk_rest_cards



def three_players(deck,number_players):
    player1 = Person("Player1",int(2))
    player2 = Person("Player2",int(2))
    player3 = Person("Player3",int(2))
    list_players = [player1,player2,player3]

    list_cards_player1 = []
    list_cards_player2 = []
    list_cards_player3 = []
    list_cards_player4 = []
    list_desk_rest_cards = []
    players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_desk_rest_cards,number_players)
    print(list_cards_player1)
    print(list_cards_player2)
    print(list_cards_player3)
    print(list_desk_rest_cards)

    card1 = Card(list_cards_player1[0])
    card2 = Card(list_cards_player1[1])
    card3 = Card(list_cards_player2[0])
    card4 = Card(list_cards_player2[1])
    card5 = Card(list_cards_player3[0])
    card6 = Card(list_cards_player3[1])
    card7 = Card(list_desk_rest_cards[0])
    card8 = Card(list_desk_rest_cards[1])
    card9 = Card(list_desk_rest_cards[2])
    card10 = Card(list_desk_rest_cards[3])
    card11 = Card(list_desk_rest_cards[4])
    card12 = Card(list_desk_rest_cards[5])
    card13 = Card(list_desk_rest_cards[6])
    card14 = Card(list_desk_rest_cards[7])
    card15 = Card(list_desk_rest_cards[8])
    list_all_cards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15]
    distribution_of_cards(list_players)







def four_players(deck,number_players):
    player1 = Person("Player1",int(2))
    player2 = Person("Player2",int(2))
    player3 = Person("Player3",int(2))
    player4 = Person("Player4",int(2))
    list_players = [player1,player2,player3,player4]

    list_cards_player1 = []
    list_cards_player2 = []
    list_cards_player3 = []
    list_cards_player4 = []
    list_desk_rest_cards = []
    players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_desk_rest_cards,number_players)
    print(list_cards_player1)
    print(list_cards_player2)
    print(list_cards_player3)
    print(list_cards_player4)
    print(list_desk_rest_cards)

    card1 = Card(list_cards_player1[0])
    card2 = Card(list_cards_player1[1])
    card3 = Card(list_cards_player2[0])
    card4 = Card(list_cards_player2[1])
    card5 = Card(list_cards_player3[0])
    card6 = Card(list_cards_player3[1])
    card7 = Card(list_cards_player4[0])
    card8 = Card(list_cards_player4[1])
    card9 = Card(list_desk_rest_cards[0])
    card10 = Card(list_desk_rest_cards[1])
    card11 = Card(list_desk_rest_cards[2])
    card12 = Card(list_desk_rest_cards[3])
    card13 = Card(list_desk_rest_cards[4])
    card14 = Card(list_desk_rest_cards[5])
    card15 = Card(list_desk_rest_cards[6])
    list_all_cards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15]
    distribution_of_cards(list_players)

    


def main():

    deck = Card("Deck")
    deck.deck_cards()
    deck.deck_random_cards()
    print(deck.LIST_RANDOM_CARDS)

 

    number_players = int(input("how many players will play this game? 3 or 4 : "))
    print("The cards can only be seen by the player of the turn")
    if number_players == 3:
        three_players(deck,number_players)
    elif number_players ==4:
        four_players(deck,number_players)

    

    


if __name__ == "__main__":
    main()
