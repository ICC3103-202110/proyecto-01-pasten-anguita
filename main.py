from card import Card
from person import Person
import random
import sys

def print_space():
    for i in range (0,20):
        print()
           
def print_challenge_or_counterattack():
    print("1-) challenge")
    print("2-) counterattack")
    print("3-) pass")
    print()

def print_counterattack():
    print("2-) counterattack")
    print("3-) pass")
    print()

def print_challenge():
    print("1-) challenge")
    print()
    print("3-) pass")

def print_actions():
    print()
    print()
    print("General actions:")
    list_all_general_actions = ["income","foreign help","coup - 7 coins"]
    for i in range(1,4):
        print(str(i)+"-)",list_all_general_actions[i-1])
    list_all_characters_actions = ["Duke-Taxes","Assassin-Assassination - 3 coins",
                                   "Captain-Extortion", "Ambassador-Change"]
    print()
    print("Characters actions: ") 
    for i in range(4,8):
        print(str(i)+"-)",list_all_characters_actions[i-4])

def print_eliminated_cards(list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                        list_eliminated_cards_player4, number_players,list_players):
    print("The cards eliminated by each palyer are:")
    print("player1: ")
    if len(list_eliminated_cards_player1) ==0:
        print()
    if len(list_eliminated_cards_player1) >0:
        for i in range(0,len(list_eliminated_cards_player1)):
            print(list_eliminated_cards_player1[i],end=' ')
    print("player2: ")
    if len(list_eliminated_cards_player2) ==0:
        print()
    if len(list_eliminated_cards_player2) >0:
        for i in range(0,len(list_eliminated_cards_player2)):
            print(list_eliminated_cards_player2[i],end=' ')
    print("player3: ")
    if len(list_eliminated_cards_player3) ==0:
        print()
    if len(list_eliminated_cards_player3) >0:
        for i in range(0,len(list_eliminated_cards_player3)):
            print(list_eliminated_cards_player3[i],end=' ')

    if number_players ==4:
        print("player4: ")
        if len(list_eliminated_cards_player4) ==0:
            print()
        if len(list_eliminated_cards_player4) >0:
            for i in range(0,len(list_eliminated_cards_player4)):
                print(list_eliminated_cards_player4[i],end=' ')

def life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players):
    if len(list_cards_player1) ==0:
        list_players[0].live_game ="no"

    if len(list_cards_player2) ==0:
        list_players[1].live_game ="no"

    if len(list_cards_player3) ==0:
        list_players[2].live_game ="no"

    if len(list_cards_player4) ==0 and number_players==4:
        list_players[3].live_game ="no"

    return(list_players)

def print_coins_players(list_players):
    for i in list_players:
        print("The coins of",i.name_person,"are:",i.coins_game)


def distribution_of_cards(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players):

    if number_players == 3:
        print("           ",list_players[0].name_person)
        print(list_players[2].name_person,"                ",list_players[1].name_person)    

    if number_players ==4:
        print(list_players[0].name_person,"         ",list_players[1].name_person)
        print(list_players[3].name_person,"         ",list_players[2].name_person)

    for i in range(0,len(list_players)):
        print(list_players[i].name_person,"Are you ready to see your cards?")
        input("Write something when you are ready: ")
        print("The cards of",list_players[i].name_person,"are :")
        print()
        if i == 0:
            for s in list_cards_player1:
                print(s)
        if i ==1:
            for s in list_cards_player2:
                print(s)
        if i ==2:
            for s in list_cards_player3:
                print(s)
        if i ==3 and number_players==4:
            for s in list_cards_player4:
                print(s)
        print()
        print()
        print("The coins of",list_players[i].name_person,"are :",list_players[i].coins_game)
        print_space()
        print(list_players[i].name_person,"look the cards, are up")
        print()
        
    print_coins_players(list_players)

def players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_rest_of_deck, number_players):
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
                list_rest_of_deck.append(i)
            count +=1
        return list_cards_player1 , list_cards_player1, list_cards_player3, list_rest_of_deck
    
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
                list_rest_of_deck.append(i)
            count +=1
        return list_cards_player1 , list_cards_player1, list_cards_player3,list_cards_player4 ,list_rest_of_deck

def player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                    list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                    list_eliminated_cards_player3, list_eliminated_cards_player4):
    if list_players[0].live_game =="yes":
        
        if selection_player1 == 2:
            list_players[0].coins_game +=2
            print("2 coins have been added for player1")
            print_coins_players(list_players)

        if selection_player1 ==3:
            for i in range(0,len(list_players)):
                if i != 0:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player1_coup =int(input("choose the player with you will use the action coup, using a number :"))
            if player1_coup ==1:
                input("player2, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player2) >0:
                    for i in range(1,len(list_cards_player2)+1):
                        print(str(i)+"-)",list_cards_player2[i-1])
                print_space()
                print("player2, look the cards, are up: ")
                select_eliminate_coup = int(input("player2, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player2[select_eliminate_coup -1]
                list_eliminated_cards_player2.append(card_eliminate_coup)
                list_cards_player2.pop(select_eliminate_coup)

            if player1_coup ==2:
                input("player3, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player3) >0:
                    for i in range(1,len(list_cards_player3)+1):
                        print(str(i)+"-)",list_cards_player3[i-1])
                print_space()
                print("player3, look the cards, are up: ")
                select_eliminate_coup = int(input("player3, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player3[select_eliminate_coup -1]
                list_eliminated_cards_player3.append(card_eliminate_coup)
                list_cards_player3.pop(select_eliminate_coup)

            if player1_coup ==3:
                input("player4, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player4) >0:
                    for i in range(1,len(list_cards_player4)+1):
                        print(str(i)+"-)",list_cards_player4[i-1])
                print_space()
                print("player4, look the cards, are up: ")
                select_eliminate_coup = int(input("player4, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player4[select_eliminate_coup -1]
                list_eliminated_cards_player4.append(card_eliminate_coup)
                list_cards_player4.pop(select_eliminate_coup)
            print("The coup action was done")

        if selection_player1 == 4:
            list_players[0].coins_game += 3
            print("3 coins have been added for player1")
            print_coins_players(list_players)
        
        if selection_player1 ==5:
            for i in range(0,len(list_players)):
                if i != 0:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player1_assassin =int(input("choose the player with you will use the action Assassin-Assassination, using a number :"))
            if player1_assassin ==1:
                input("player2, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player2) > 0:
                    for s in range(1,len(list_cards_player2)+1):
                        print(str(s)+"-)", list_cards_player2[s-1])
                print_space()
                print("player2, look the cards, are up")
                eliminate_card_player2 = int(input("player2, select the card that you want delete, using a number : "))
                list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
                list_cards_player2.pop(eliminate_card_player2-1)

            if player1_assassin ==2:
                input("player3, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player3)>0:
                    for s in range(1,len(list_cards_player3)+1):
                        print(str(s)+"-)", list_cards_player3[s-1])
                print_space()
                print("player3, look the cards, are up")
                eliminate_card_player3 = int(input("player3, select the card that you want delete, using a number : "))
                list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
                list_cards_player3.pop(eliminate_card_player3-1)

            if player1_assassin ==3:
                input("player4, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player4)>0:
                    for s in range(1,len(list_cards_player4)+1):
                        print(str(s)+"-)", list_cards_player4[s-1])
                print_space()
                print("player4, look the cards, are up")
                eliminate_card_player4 = int(input("player4, select the card that you want delete, using a number : "))
                list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
                list_cards_player4.pop(eliminate_card_player4-1)

        if selection_player1 ==6:
            print_coins_players(list_players)
            for i in range(0,len(list_players)):
                if i != 0:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            
            player1_captain =int(input("Player1, choose the player with you will use the action Captain-Extortion, using a number :"))
            if player1_captain ==1:
                if list_players[1].coins_game <1:
                    print("The player1 +0 coins")
                    print("The player2 -0 coins")

                if list_players[1].coins_game ==1 :
                    list_players[1].coins_game -= 1
                    list_players[0].coins_game +=1
                    print("The player1 +1 coins")
                    print("The player2 -1 coins")

                if list_players[1].coins_game >= 2:
                    list_players[1].coins_game -=2
                    list_players[0].coins_game +=2
                    print("The player1 +2 coins")
                    print("The player2 -2 coins")

            if player1_captain ==2:
                if list_players[2].coins_game <1:
                    print("The player1 +0 coins")
                    print("The player3 -0 coins")

                if list_players[2].coins_game ==1 :
                    list_players[2].coins_game -= 1
                    list_players[0].coins_game +=1
                    print("The player1 +1 coins")
                    print("The player3 -1 coins")

                if list_players[2].coins_game >= 2:
                    list_players[2].coins_game -=2
                    list_players[0].coins_game +=2
                    print("The player1 +2 coins")
                    print("The player3 -3 coins")

            if player1_captain ==3:
                if list_players[3].coins_game <1:
                    print("The player1 +0 coins")
                    print("The player4 -0 coins")

                if list_players[3].coins_game ==1 :
                    list_players[3].coins_game -= 1
                    list_players[0].coins_game +=1
                    print("The player1 +1 coins")
                    print("The player4 -1 coins")

                if list_players[3].coins_game >= 2:
                    list_players[3].coins_game -=2
                    list_players[0].coins_game +=2
                    print("The player1 +2 coins")
                    print("The player4 -3 coins")    
       
            print_coins_players(list_players)
   
        if selection_player1 ==7:
            print()
            input("player1, are you ready to do the action 'Ambassador-Change'?, write something when you are ready: ")

            if len(list_cards_player1) ==1:
                print("1-)",list_cards_player1[0])    
                print("2-)",list_rest_of_deck[0])
                print("3-)",list_rest_of_deck[1])
        
            if len(list_cards_player1) ==2:
                print("1-)", list_cards_player1[0])
                print("2-)", list_cards_player1[1])
                print("3-)", list_rest_of_deck[0])
                print("4-)", list_rest_of_deck[1])
            while True:
                ambassador_player1_1 =int(input("Select the first card that you want, using a number: "))
                ambassador_player1_2 =int(input("Select the second card that you want (you can't select the same card), using a number: "))
                if ambassador_player1_1 == ambassador_player1_2:
                    print("you can't repeat the cards, do it again")
                if ambassador_player1_1 != ambassador_player1_2:
                    break
            
            list_cards_player1_2 =[]
            if len(list_cards_player1) ==1:
                if ambassador_player1_1 == 1:
                    list_cards_player1_2.append(list_cards_player1[0])
                if ambassador_player1_1 > 1:
                    list_cards_player1_2.append(list_rest_of_deck[ambassador_player1_1 - 2])
                    list_rest_of_deck.pop(ambassador_player1_1 - 2)

                if ambassador_player1_2 ==1:
                    list_cards_player1_2.append(list_cards_player1[0])
                if ambassador_player1_2 >1:
                    list_cards_player1_2.append(list_rest_of_deck[ambassador_player1_2 - 2])
                    if ambassador_player1_1 <2:
                        list_rest_of_deck.pop(ambassador_player1_2 - 2)
                    if ambassador_player1_1 ==2:
                        list_rest_of_deck.pop(0)

            if len(list_cards_player1) ==2:
                if ambassador_player1_1 <=2:
                    list_cards_player1_2.append(list_cards_player1[ambassador_player1_1 - 1])
                if ambassador_player1_1 > 2:
                    list_cards_player1_2.append(list_rest_of_deck[ambassador_player1_1 - 3])
                    list_rest_of_deck.pop(ambassador_player1_1 - 3)

                if ambassador_player1_2 <=2:
                    list_cards_player1_2.append(list_cards_player1[ambassador_player1_2 - 1])
                if ambassador_player1_2 > 2:
                    list_cards_player1_2.append(list_rest_of_deck[ambassador_player1_2 - 3])
                    if ambassador_player1_1 <3:
                        list_rest_of_deck.pop(ambassador_player1_2 - 3)
                    if ambassador_player1_1 ==3:
                        list_rest_of_deck.pop(0)
            count= 0
            for i in list_cards_player1:
                if i != list_cards_player1_2[count]:
                    list_rest_of_deck.append(i)
                count +=1
            list_cards_player1 = list_cards_player1_2
            list_cards_player1_2 = []

    return(list_players,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
            list_eliminated_cards_player3, list_eliminated_cards_player4)

def player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                    list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                    list_eliminated_cards_player3, list_eliminated_cards_player4):
    if list_players[1].live_game =="yes":
        if selection_player2 == 2:
            list_players[1].coins_game +=2
            print("2 coins have been added for player1")
            print_coins_players(list_players)

        if selection_player2 ==3:
            for i in range(0,len(list_players)):
                if i != 1: 
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player2_coup =int(input("choose the player with whom you will use the action coup, using a number :"))
            if player2_coup ==0:
                input("player1, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player1) >0:
                    for i in range(1,len(list_cards_player1)+1):
                        print(str(i)+"-)",list_cards_player1[i-1])
                print_space()
                print("player1, scroll up to see your cards. ")
                select_eliminate_coup = int(input("player1, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player1[select_eliminate_coup -1]
                list_eliminated_cards_player1.append(card_eliminate_coup)
                list_cards_player1.pop(select_eliminate_coup)

            if player2_coup ==2:
                input("player3, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player3) >0:
                    for i in range(1,len(list_cards_player3)+1):
                        print(str(i)+"-)",list_cards_player3[i-1])
                print_space()
                print("player3, scroll up to see your cards.")
                select_eliminate_coup = int(input("player3, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player3[select_eliminate_coup -1]
                list_eliminated_cards_player3.append(card_eliminate_coup)
                list_cards_player3.pop(select_eliminate_coup)

            if player2_coup ==3:
                input("player4, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player4) >0:
                    for i in range(1,len(list_cards_player4)+1):
                        print(str(i)+"-)",list_cards_player4[i-1])
                print_space()
                print("player4, scroll up to see your cards.")
                select_eliminate_coup = int(input("player4, select the card that you want to turn over, using a number:"))
                card_eliminate_coup = list_cards_player4[select_eliminate_coup -1]
                list_eliminated_cards_player4.append(card_eliminate_coup)
                list_cards_player4.pop(select_eliminate_coup)
            print("The coup action was done")

    
        if selection_player2 == 4:
            list_players[1].coins_game += 3
            print("3 coins have been added for player2")
            print_coins_players(list_players)

        
        if selection_player2 ==5:
            for i in range(0,len(list_players)):
                if i != 1:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player2_assassin =int(input("choose the player with whom you will use the action Assassin-Assassination, using a number :"))
            if player2_assassin ==0:
                input("player1, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player1) > 0:
                    for s in range(1,len(list_cards_player1)+1):
                        print(str(s)+"-)", list_cards_player1[s-1])
                print_space()
                print("player1, scroll up to see your cards.")
                eliminate_card_player1 = int(input("player1, select the card that you want delete, using a number : "))
                list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
                list_cards_player1.pop(eliminate_card_player1-1)

            if player2_assassin ==2:
                input("player3, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player3)>0:
                    for s in range(1,len(list_cards_player3)+1):
                        print(str(s)+"-)", list_cards_player3[s-1])
                print_space()
                print("player3, scroll up to see your cards")
                eliminate_card_player3 = int(input("player3, select the card that you want delete, using a number : "))
                list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
                list_cards_player3.pop(eliminate_card_player3-1)

            if player2_assassin ==3:
                input("player4, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player4)>0:
                    for s in range(1,len(list_cards_player4)+1):
                        print(str(s)+"-)", list_cards_player4[s-1])
                print_space()
                print("player4, scroll up to see your cards.")
                eliminate_card_player4 = int(input("player4, select the card that you want delete, using a number : "))
                list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
                list_cards_player4.pop(eliminate_card_player4-1)

        if selection_player2 ==6:
            print_coins_players(list_players)
            for i in range(0,len(list_players)):
                if i != 1:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            
            player2_captain =int(input("Player2, choose the player with whom you will use the action Captain-Extortion, using a number :"))
            if player2_captain ==0:
                if list_players[1].coins_game <1:
                    print("Player2: +0 coins")
                    print("Player1: -0 coins")

                if list_players[0].coins_game ==1 :
                    list_players[0].coins_game -= 1
                    list_players[1].coins_game +=1
                    print("Player2: +1 coins")
                    print("Player1: -1 coins")

                if list_players[0].coins_game >= 2:
                    list_players[0].coins_game -=2
                    list_players[1].coins_game +=2
                    print("Player2: +2 coins")
                    print("Player1: -2 coins")

            if player2_captain ==2:
                if list_players[2].coins_game <1:
                    print("Player2: +0 coins")
                    print("Player3: -0 coins")

                if list_players[2].coins_game ==1 :
                    list_players[2].coins_game -= 1
                    list_players[1].coins_game +=1
                    print("Player2: +1 coins")
                    print("Player3: -1 coins")

                if list_players[2].coins_game >= 2:
                    list_players[2].coins_game -=2
                    list_players[1].coins_game +=2
                    print("Player2: +2 coins")
                    print("Player3: -3 coins")

            if player2_captain ==3:
                if list_players[3].coins_game <1:
                    print("Player2: +0 coins")
                    print("Player4: -0 coins")

                if list_players[3].coins_game ==1 :
                    list_players[3].coins_game -= 1
                    list_players[1].coins_game +=1
                    print("Player2: +1 coins")
                    print("Player4: -1 coins")

                if list_players[3].coins_game >= 2:
                    list_players[3].coins_game -=2
                    list_players[1].coins_game +=2
                    print("Player2: +2 coins")
                    print("Player4: -3 coins")    
       
            print_coins_players(list_players)
   
        if selection_player2 ==7:
            print()
            input("player2, are you ready to do the action 'Ambassador-Exchange'?, write something when you are ready: ")

            if len(list_cards_player2) ==1:
                print("1-)",list_cards_player2[0])    
                print("2-)",list_rest_of_deck[0])
                print("3-)",list_rest_of_deck[1])
        
            if len(list_cards_player2) ==2:
                print("1-)", list_cards_player2[0])
                print("2-)", list_cards_player2[1])
                print("3-)", list_rest_of_deck[0])
                print("4-)", list_rest_of_deck[1])
            while True:
                ambassador_player2_1 =int(input("Select the first card that you want, using a number: "))
                ambassador_player2_2 =int(input("Select the second card that you want (you can't select the same card), using a number: "))
                if ambassador_player2_1 == ambassador_player2_2:
                    print("you can't repeat the cards, do it again")
                if ambassador_player2_1 != ambassador_player2_2:
                    break
            
            list_cards_player2_2 =[]
            if len(list_cards_player2) ==1:
                if ambassador_player2_1 == 1:
                    list_cards_player2_2.append(list_cards_player2[0])
                if ambassador_player2_1 > 1:
                    list_cards_player2_2.append(list_rest_of_deck[ambassador_player2_1 - 2])
                    list_rest_of_deck.pop(ambassador_player2_1 - 2)

                if ambassador_player2_2 ==1:
                    list_cards_player2_2.append(list_cards_player2[0])
                if ambassador_player2_2 >1:
                    list_cards_player2_2.append(list_rest_of_deck[ambassador_player2_2 - 2])
                    if ambassador_player2_1 <2: 
                        list_rest_of_deck.pop(ambassador_player2_2 - 2)
                    if ambassador_player2_1 ==2:
                        list_rest_of_deck.pop(0)

            if len(list_cards_player2) ==2:
                if ambassador_player2_1 <=2:
                    list_cards_player2_2.append(list_cards_player2[ambassador_player2_1 - 1])
                if ambassador_player2_1 > 2:
                    list_cards_player2_2.append(list_rest_of_deck[ambassador_player2_1 - 3])
                    list_rest_of_deck.pop(ambassador_player2_1 - 3)

                if ambassador_player2_2 <=2:
                    list_cards_player2_2.append(list_cards_player2[ambassador_player2_2 - 1])
                if ambassador_player2_2 > 2:
                    list_cards_player2_2.append(list_rest_of_deck[ambassador_player2_2 - 3])
                    if ambassador_player2_1 <3:
                        list_rest_of_deck.pop(ambassador_player2_2 - 3)
                    if ambassador_player2_1 ==3:
                        list_rest_of_deck.pop(0)
            count= 0
            for i in list_cards_player2:
                if i != list_cards_player2_2[count]:
                    list_rest_of_deck.append(i)
                count +=1
            list_cards_player2 = list_cards_player2_2
            list_cards_player2_2 = []

    return(list_players,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
            list_eliminated_cards_player3, list_eliminated_cards_player4)

def player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                    list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                    list_eliminated_cards_player3, list_eliminated_cards_player4):
    if list_players[2].live_game =="yes":
        if selection_player3 == 2:
            list_players[2].coins_game +=2
            print("2 coins have been added for player3")
            print_coins_players(list_players)

        if selection_player3 ==3:
            for i in range(0,len(list_players)):
                if i != 2: 
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player3_coup =int(input("choose the player with whom you will use the action coup, using a number :"))
            if player3_coup ==0:
                input("player1, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player1) >0:
                    for i in range(1,len(list_cards_player1)+1):
                        print(str(i)+"-)",list_cards_player1[i-1])
                print_space()
                print("player1, scroll up to see your cards. ")
                select_eliminate_coup = int(input("player1, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player1[select_eliminate_coup -1]
                list_eliminated_cards_player1.append(card_eliminate_coup)
                list_cards_player1.pop(select_eliminate_coup)

            if player3_coup ==1:
                input("player2, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player2) >0:
                    for i in range(1,len(list_cards_player2)+1):
                        print(str(i)+"-)",list_cards_player2[i-1])
                print_space()
                print("player2, scroll up to see your cards.")
                select_eliminate_coup = int(input("player2, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player2[select_eliminate_coup -1]
                list_eliminated_cards_player2.append(card_eliminate_coup)
                list_cards_player2.pop(select_eliminate_coup)

            if player3_coup ==3:
                input("player4, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player4) >0:
                    for i in range(1,len(list_cards_player4)+1):
                        print(str(i)+"-)",list_cards_player4[i-1])
                print_space()
                print("player4, scroll up to see your cards.")
                select_eliminate_coup = int(input("player4, select the card that you want to turn over, using a number:"))
                card_eliminate_coup = list_cards_player4[select_eliminate_coup -1]
                list_eliminated_cards_player4.append(card_eliminate_coup)
                list_cards_player4.pop(select_eliminate_coup)
            print("The coup action was done")

    
        if selection_player3 == 4:
            list_players[2].coins_game += 3
            print("3 coins have been added for player3")
            print_coins_players(list_players)

        
        if selection_player3 ==5:
            for i in range(0,len(list_players)):
                if i != 2:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player3_assassin =int(input("choose the player with whom you will use the action Assassin-Assassination, using a number :"))
            if player3_assassin ==0:
                input("player1, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player1) > 0:
                    for s in range(1,len(list_cards_player1)+1):
                        print(str(s)+"-)", list_cards_player1[s-1])
                print_space()
                print("player1, scroll up to see your cards.")
                eliminate_card_player1 = int(input("player1, select the card that you want delete, using a number : "))
                list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
                list_cards_player1.pop(eliminate_card_player1-1)

            if player3_assassin ==1:
                input("player2, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player2)>0:
                    for s in range(1,len(list_cards_player2)+1):
                        print(str(s)+"-)", list_cards_player2[s-1])
                print_space()
                print("player2, scroll up to see your cards")
                eliminate_card_player2 = int(input("player2, select the card that you want delete, using a number : "))
                list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
                list_cards_player2.pop(eliminate_card_player2-1)

            if player3_assassin ==3:
                input("player4, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player4)>0:
                    for s in range(1,len(list_cards_player4)+1):
                        print(str(s)+"-)", list_cards_player4[s-1])
                print_space()
                print("player4, scroll up to see your cards.")
                eliminate_card_player4 = int(input("player4, select the card that you want delete, using a number : "))
                list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
                list_cards_player4.pop(eliminate_card_player4-1)

        if selection_player3 ==6:
            print_coins_players(list_players)
            for i in range(0,len(list_players)):
                if i != 2:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            
            player3_captain =int(input("Player3, choose the player with whom you will use the action Captain-Extortion, using a number :"))
            if player3_captain ==0:
                if list_players[0].coins_game <1:
                    print("Player3: +0 coins")
                    print("Player1: -0 coins")

                if list_players[0].coins_game ==1 :
                    list_players[0].coins_game -= 1
                    list_players[2].coins_game +=1
                    print("Player3: +1 coins")
                    print("Player1: -1 coins")

                if list_players[0].coins_game >= 2:
                    list_players[0].coins_game -=2
                    list_players[2].coins_game +=2
                    print("Player3: +2 coins")
                    print("Player1: -2 coins")

            if player3_captain ==1:
                if list_players[1].coins_game <1:
                    print("Player3: +0 coins")
                    print("Player2: -0 coins")

                if list_players[1].coins_game ==1 :
                    list_players[1].coins_game -= 1
                    list_players[2].coins_game +=1
                    print("Player3: +1 coins")
                    print("Player2: -1 coins")

                if list_players[1].coins_game >= 2:
                    list_players[1].coins_game -=2
                    list_players[2].coins_game +=2
                    print("Player3: +2 coins")
                    print("Player2: -2 coins")

            if player3_captain ==3:
                if list_players[3].coins_game <1:
                    print("Player3: +0 coins")
                    print("Player4: -0 coins")

                if list_players[3].coins_game ==1 :
                    list_players[3].coins_game -= 1
                    list_players[2].coins_game +=1
                    print("Player3: +1 coins")
                    print("Player4: -1 coins")

                if list_players[3].coins_game >= 2:
                    list_players[3].coins_game -=2
                    list_players[1].coins_game +=2
                    print("Player2: +2 coins")
                    print("Player4: -2 coins")    
       
            print_coins_players(list_players)
   
        if selection_player3 ==7:
            print()
            input("player3, are you ready to do the action 'Ambassador-Exchange'?, write something when you are ready: ")

            if len(list_cards_player3) ==1:
                print("1-)",list_cards_player3[0])    
                print("2-)",list_rest_of_deck[0])
                print("3-)",list_rest_of_deck[1])
        
            if len(list_cards_player3) ==2:
                print("1-)", list_cards_player3[0])
                print("2-)", list_cards_player3[1])
                print("3-)", list_rest_of_deck[0])
                print("4-)", list_rest_of_deck[1])
            while True:
                ambassador_player3_1 =int(input("Select the first card that you want, using a number: "))
                ambassador_player3_2 =int(input("Select the second card that you want (you can't select the same card), using a number: "))
                if ambassador_player3_1 == ambassador_player3_2:
                    print("you can't repeat the cards, do it again")
                if ambassador_player3_1 != ambassador_player3_2:
                    break
            
            list_cards_player3_2 =[]
            if len(list_cards_player3) ==1:
                if ambassador_player3_1 == 1:
                    list_cards_player3_2.append(list_cards_player3[0])
                if ambassador_player3_1 > 1:
                    list_cards_player3_2.append(list_rest_of_deck[ambassador_player3_1 - 2])
                    list_rest_of_deck.pop(ambassador_player3_1 - 2)

                if ambassador_player3_2 ==1:
                    list_cards_player3_2.append(list_cards_player3[0])
                if ambassador_player3_2 >1:
                    list_cards_player3_2.append(list_rest_of_deck[ambassador_player3_2 - 2])
                    if ambassador_player3_1 <2: 
                        list_rest_of_deck.pop(ambassador_player3_2 - 2)
                    if ambassador_player3_1 ==2:
                        list_rest_of_deck.pop(0)

            if len(list_cards_player3) ==2:
                if ambassador_player3_1 <=2:
                    list_cards_player3_2.append(list_cards_player3[ambassador_player3_1 - 1])
                if ambassador_player3_1 > 2:
                    list_cards_player3_2.append(list_rest_of_deck[ambassador_player3_1 - 3])
                    list_rest_of_deck.pop(ambassador_player3_1 - 3)

                if ambassador_player3_2 <=2:
                    list_cards_player3_2.append(list_cards_player3[ambassador_player3_2 - 1])
                if ambassador_player3_2 > 2:
                    list_cards_player3_2.append(list_rest_of_deck[ambassador_player3_2 - 3])
                    if ambassador_player3_1 <3:
                        list_rest_of_deck.pop(ambassador_player3_2 - 3)
                    if ambassador_player3_1 ==3:
                        list_rest_of_deck.pop(0)
            count= 0 
            for i in list_cards_player3:
                if i != list_cards_player3_2[count]:
                    list_rest_of_deck.append(i)
                count +=1
            list_cards_player3 = list_cards_player3_2
            list_cards_player3_2 = []

    return(list_players,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
            list_eliminated_cards_player3, list_eliminated_cards_player4)

def player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                    list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                    list_eliminated_cards_player3, list_eliminated_cards_player4):
  if number_players==4:  
    if list_players[3].live_game =="yes":
        if selection_player3 == 2:
            list_players[3].coins_game +=2
            print("2 coins have been added for player4")
            print_coins_players(list_players)

        if selection_player4 ==3:
            for i in range(0,len(list_players)):
                if i != 3: 
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player4_coup =int(input("choose the player with whom you will use the action coup, using a number :"))
            if player4_coup ==0:
                input("player1, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player1) >0:
                    for i in range(1,len(list_cards_player1)+1):
                        print(str(i)+"-)",list_cards_player1[i-1])
                print_space()
                print("player1, scroll up to see your cards. ")
                select_eliminate_coup = int(input("player1, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player1[select_eliminate_coup -1]
                list_eliminated_cards_player1.append(card_eliminate_coup)
                list_cards_player1.pop(select_eliminate_coup)

            if player4_coup ==1:
                input("player2, are you ready to see your cards? Write something when you are ready: ")
                if len(list_cards_player2) >0:
                    for i in range(1,len(list_cards_player2)+1):
                        print(str(i)+"-)",list_cards_player2[i-1])
                print_space()
                print("player2, scroll up to see your cards.")
                select_eliminate_coup = int(input("player2, select the card that you want delete, using a number:"))
                card_eliminate_coup = list_cards_player2[select_eliminate_coup -1]
                list_eliminated_cards_player2.append(card_eliminate_coup)
                list_cards_player2.pop(select_eliminate_coup)

            if player4_coup ==2:
                input("player3, are you ready to see your cards, write something when you are ready: ")
                if len(list_cards_player3) >0:
                    for i in range(1,len(list_cards_player3)+1):
                        print(str(i)+"-)",list_cards_player3[i-1])
                print_space()
                print("player3, scroll up to see your cards.")
                select_eliminate_coup = int(input("player3, select the card that you want to turn over, using a number:"))
                card_eliminate_coup = list_cards_player3[select_eliminate_coup -1]
                list_eliminated_cards_player3.append(card_eliminate_coup)
                list_cards_player3.pop(select_eliminate_coup)
            print("The coup action was done")

    
        if selection_player4 == 4:
            list_players[3].coins_game += 3
            print("3 coins have been added for player3")
            print_coins_players(list_players)

        
        if selection_player4 ==5:
            for i in range(0,len(list_players)):
                if i != 3:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            player4_assassin =int(input("choose the player with whom you will use the action Assassin-Assassination, using a number :"))
            if player4_assassin ==0:
                input("player1, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player1) > 0:
                    for s in range(1,len(list_cards_player1)+1):
                        print(str(s)+"-)", list_cards_player1[s-1])
                print_space()
                print("player1, scroll up to see your cards.")
                eliminate_card_player1 = int(input("player1, select the card that you want delete, using a number : "))
                list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
                list_cards_player1.pop(eliminate_card_player1-1)

            if player4_assassin ==1:
                input("player2, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player2)>0:
                    for s in range(1,len(list_cards_player2)+1):
                        print(str(s)+"-)", list_cards_player2[s-1])
                print_space()
                print("player2, scroll up to see your cards")
                eliminate_card_player2 = int(input("player2, select the card that you want delete, using a number : "))
                list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
                list_cards_player2.pop(eliminate_card_player2-1)

            if player4_assassin ==2:
                input("player3, are you ready to see your cards?, write something when you are ready: ")
                if len(list_cards_player3)>0:
                    for s in range(1,len(list_cards_player3)+1):
                        print(str(s)+"-)", list_cards_player3[s-1])
                print_space()
                print("player3, scroll up to see your cards.")
                eliminate_card_player3 = int(input("player3, select the card that you want delete, using a number : "))
                list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
                list_cards_player3.pop(eliminate_card_player4-1)

        if selection_player4 ==6:
            print_coins_players(list_players)
            for i in range(0,len(list_players)):
                if i != 3:
                    if list_players[i].live_game =="yes":
                        print(str(i)+"-)", list_players[i].name_person)
            
            player4_captain =int(input("Player4, choose the player with whom you will use the action Captain-Extortion, using a number :"))
            if player4_captain ==0:
                if list_players[0].coins_game <1:
                    print("Player4: +0 coins")
                    print("Player1: -0 coins")

                if list_players[0].coins_game ==1 :
                    list_players[0].coins_game -= 1
                    list_players[3].coins_game +=1
                    print("Player4: +1 coins")
                    print("Player1: -1 coins")

                if list_players[0].coins_game >= 2:
                    list_players[0].coins_game -=2
                    list_players[3].coins_game +=2
                    print("Player4: +2 coins")
                    print("Player1: -2 coins")

            if player4_captain ==1:
                if list_players[1].coins_game <1:
                    print("Player4: +0 coins")
                    print("Player2: -0 coins")

                if list_players[1].coins_game ==1 :
                    list_players[1].coins_game -= 1
                    list_players[3].coins_game +=1
                    print("Player4: +1 coins")
                    print("Player2: -1 coins")

                if list_players[1].coins_game >= 2:
                    list_players[1].coins_game -=2
                    list_players[3].coins_game +=2
                    print("Player4: +2 coins")
                    print("Player2: -2 coins")

            if player4_captain ==2:
                if list_players[2].coins_game <1:
                    print("Player4: +0 coins")
                    print("Player3: -0 coins")

                if list_players[2].coins_game ==1 :
                    list_players[2].coins_game -= 1
                    list_players[3].coins_game +=1
                    print("Player4: +1 coins")
                    print("Player3: -1 coins")

                if list_players[2].coins_game >= 2:
                    list_players[2].coins_game -=2
                    list_players[3].coins_game +=2
                    print("Player4: +2 coins")
                    print("Player3: -2 coins")    
       
            print_coins_players(list_players)
   
        if selection_player4 ==7:
            print()
            input("player4, are you ready to do the action 'Ambassador-Exchange'?, write something when you are ready: ")

            if len(list_cards_player4) ==1:
                print("1-)",list_cards_player4[0])    
                print("2-)",list_rest_of_deck[0])
                print("3-)",list_rest_of_deck[1])
        
            if len(list_cards_player4) ==2:
                print("1-)", list_cards_player4[0])
                print("2-)", list_cards_player4[1])
                print("3-)", list_rest_of_deck[0])
                print("4-)", list_rest_of_deck[1])
            while True:
                ambassador_player4_1 =int(input("Select the first card that you want, using a number: "))
                ambassador_player4_2 =int(input("Select the second card that you want (you can't select the same card), using a number: "))
                if ambassador_player4_1 == ambassador_player4_2:
                    print("you can't repeat the cards, do it again")
                if ambassador_player4_1 != ambassador_player4_2:
                    break
            
            list_cards_player4_2 =[]
            if len(list_cards_player4) ==1:
                if ambassador_player4_1 == 1:
                    list_cards_player4_2.append(list_cards_player4[0])
                if ambassador_player4_1 > 1:
                    list_cards_player4_2.append(list_rest_of_deck[ambassador_player4_1 - 2])
                    list_rest_of_deck.pop(ambassador_player4_1 - 2)

                if ambassador_player4_2 ==1:
                    list_cards_player4_2.append(list_cards_player4[0])
                if ambassador_player4_2 >1:
                    list_cards_player4_2.append(list_rest_of_deck[ambassador_player4_2 - 2])
                    if ambassador_player4_1 <2: 
                        list_rest_of_deck.pop(ambassador_player4_2 - 2)
                    if ambassador_player4_1 ==2:
                        list_rest_of_deck.pop(0)

            if len(list_cards_player4) ==2:
                if ambassador_player4_1 <=2:
                    list_cards_player4_2.append(list_cards_player4[ambassador_player4_1 - 1])
                if ambassador_player4_1 > 2:
                    list_cards_player4_2.append(list_rest_of_deck[ambassador_player4_1 - 3])
                    list_rest_of_deck.pop(ambassador_player4_1 - 3)

                if ambassador_player4_2 <=2:
                    list_cards_player4_2.append(list_cards_player4[ambassador_player4_2 - 1])
                if ambassador_player4_2 > 2:
                    list_cards_player4_2.append(list_rest_of_deck[ambassador_player4_2 - 3])
                    if ambassador_player4_1 <3:
                        list_rest_of_deck.pop(ambassador_player4_2 - 3)
                    if ambassador_player4_1 ==3:
                        list_rest_of_deck.pop(0)
            count= 0 
            for i in list_cards_player4:
                if i != list_cards_player4_2[count]:
                    list_rest_of_deck.append(i)
                count +=1
            list_cards_player4 = list_cards_player4_2
            list_cards_player4_2 = []

    return(list_players,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
            list_eliminated_cards_player3, list_eliminated_cards_player4)
                
def counterattack_player1(random_1,selection_player1,list_situation_player1_counterattack,list_cards_player1,list_cards_player2,
                            list_cards_player3,list_cards_player4,number_players,list_eliminated_cards_player1,
                            list_eliminated_cards_player2,list_eliminated_cards_player3,list_eliminated_cards_player4,list_players):
    #quien contraataca (random_1)
    if random_1 ==2:
        print("Player2 will counterattack player1")
    if random_1 ==3:
        print("Player3 will counterattack player1")
    if number_players ==4 and random_1 ==4:
        print("Player4 will counterattack player1")

    print_challenge()
    #pasar o desafiar contraataque
    selection_player1_2 = int(input("Player1, what do you want to do against the counterattack? Select a option using a number: "))
    #pasar
    if selection_player1_2 == 3:
        print("Player1's action was countered succesfully")
        situation_player1_counterattack = "lose"
        list_situation_player1_counterattack.append(situation_player1_counterattack)
    #desafiar
    if selection_player1_2 ==1:
        #jugador de turno desafía los contraataquesa los demás
        if random_1 ==2:
            input("player2, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player2) >0:
                for i in range(1,len(list_cards_player2) + 1):
                    print(str(i)+"-)", list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards.")
            select_counterattack =int(input("Player2 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player2[select_counterattack-1]

        if random_1 ==3:
            input("Player3, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player3) >0:
                for i in range(1,len(list_cards_player3) + 1):
                    print(str(i)+"-)", list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards")
            select_counterattack =int(input("Player3 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player3[select_counterattack-1]

        if random_1 ==4:
            input("Player4, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4) + 1):
                    print(str(i)+"-)", list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards")
            select_counterattack =int(input("Player4 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player4[select_counterattack-1]
        #contraataque  a foreign help:
        if selection_player1 ==2:
            if select_card_counterattack =="Duke":
                print("Player1 was countered succesfully with the card 'Duke'")
                situation_player1_counterattack = "lose"
        
            if select_card_counterattack !="Duke":
                print("The player that counterattacked doesn't have the card 'Duke'")
                situation_player1_counterattack ="win"
        #contraataque al asesino:
        if selection_player1 ==5:
            if select_card_counterattack =="Countess":
                print("Player1 was countered succesfully with the card 'Countess'")
                situation_player1_counterattack = "lose"
        
            if select_card_counterattack !="Countess":
                print("The player that counterattacked doesn't have de card 'Countess'")
                situation_player1_counterattack ="win"
        #contraataque al capitan (steal)
        if selection_player1 ==6:
            if select_card_counterattack =="Ambassador" or select_card_counterattack =="Captain":
                print("Player1 was countered succesfully with the card", select_card_counterattack)
                situation_player1_counterattack = "lose"
        
            else:
                print("The player that counterattacked doesn't have the card 'Captain' or 'Ambassador'")
                situation_player1_counterattack ="win"

        #devolver cartas usadas al maso:
        list_situation_player1_counterattack.append(situation_player1_counterattack)
        if situation_player1_counterattack =="win":
            if random_1 ==2:
                list_eliminated_cards_player2.append(select_card_counterattack)
                list_cards_player2.pop(select_counterattack -1)
            if random_1 ==3:
                list_eliminated_cards_player3.append(select_card_counterattack)
                list_cards_player3.pop(select_counterattack -1)
            if random_1 ==4:
                list_eliminated_cards_player4.append(select_card_counterattack)
                list_cards_player4.pop(select_counterattack -1)

        if situation_player1_counterattack =="lose":
            input("player1, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1) + 1):
                    print(str(i)+"-)", list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards")
            select_eliminate =int(input("player1 ,select the card that you prefer to lose, using a number: "))
            eliminate_card = list_cards_player1[select_eliminate-1]
            list_eliminated_cards_player1.append(eliminate_card)
            list_cards_player1.pop(select_eliminate-1)

        life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

    return(list_situation_player1_counterattack,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4, list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
            list_eliminated_cards_player4, list_players)

def counterattack_player2(random_2,selection_player2,list_situation_player2_counterattack,list_cards_player1,list_cards_player2,
                            list_cards_player3,list_cards_player4,number_players,list_eliminated_cards_player1,
                            list_eliminated_cards_player2,list_eliminated_cards_player3,list_eliminated_cards_player4,list_players):
    #quien contraataca (random_2)
    if random_2 ==1:
        print("Player1 will counterattack player2")
    if random_2 ==3:
        print("Player3 will counterattack player2")
    if number_players ==4 and random_2 ==4:
        print("Player4 will counterattack player2")

    print_challenge()
    #pasar o desafiar contraataque
    selection_player2_2 = int(input("Player2, what do you want to do against the counterattack? Select a option using a number: "))
    #pasar
    if selection_player2_2 == 3:
        print("Player2's action was countered succesfully.")
        situation_player2_counterattack = "lose"
        list_situation_player2_counterattack.append(situation_player2_counterattack)
    #desafiar
    if selection_player2_2 ==1:
        #jugador de turno desafía los contraataquesa los demás
        if random_2 ==1:
            input("player1, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1) + 1):
                    print(str(i)+"-)", list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards.")
            select_counterattack =int(input("Player1 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player1[select_counterattack-1]

        if random_2 ==3:
            input("Player3, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player3) >0:
                for i in range(1,len(list_cards_player3) + 1):
                    print(str(i)+"-)", list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards")
            select_counterattack =int(input("Player3 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player3[select_counterattack-1]

        if random_2 ==4:
            input("Player4, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4) + 1):
                    print(str(i)+"-)", list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards")
            select_counterattack =int(input("Player4 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player4[select_counterattack-1]
        #contraataque  a foreign help:
        if selection_player2 ==2:
            if select_card_counterattack =="Duke":
                print("Player2 was countered succesfully with the card 'Duke'")
                situation_player2_counterattack = "lose"
        
            if select_card_counterattack !="Duke":
                print("The player that counterattacked doesn't have the card 'Duke'")
                situation_player2_counterattack ="win"
        #contraataque al asesino:
        if selection_player2 ==5:
            if select_card_counterattack =="Countess":
                print("Player2 was countered succesfully with the card 'Countess'")
                situation_player2_counterattack = "lose"
        
            if select_card_counterattack !="Countess":
                print("The player that counterattacked doesn't have de card 'Countess'")
                situation_player2_counterattack ="win"
        #contraataque al capitan (steal)
        if selection_player2 ==6:
            if select_card_counterattack =="Ambassador" or select_card_counterattack =="Captain":
                print("Player2 was countered succesfully with the card", select_card_counterattack)
                situation_player2_counterattack = "lose"
        
            else:
                print("The player that counterattacked doesn't have the card 'Captain' or 'Ambassador'")
                situation_player2_counterattack ="win"

        #devolver cartas usadas al maso:
        list_situation_player2_counterattack.append(situation_player2_counterattack)
        if situation_player2_counterattack =="win":
            if random_2 ==1:
                list_eliminated_cards_player1.append(select_card_counterattack)
                list_cards_player1.pop(select_counterattack -1)
            if random_2 ==3:
                list_eliminated_cards_player3.append(select_card_counterattack)
                list_cards_player3.pop(select_counterattack -1)
            if random_2 ==4:
                list_eliminated_cards_player4.append(select_card_counterattack)
                list_cards_player4.pop(select_counterattack -1)

        if situation_player2_counterattack =="lose":
            input("player2, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player2) >0:
                for i in range(1,len(list_cards_player2) + 1):
                    print(str(i)+"-)", list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards")
            select_eliminate =int(input("player2 ,select the card that you prefer to lose, using a number: "))
            eliminate_card = list_cards_player2[select_eliminate-1]
            list_eliminated_cards_player2.append(eliminate_card)
            list_cards_player2.pop(select_eliminate-1)

        life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

    return(list_situation_player2_counterattack,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4, list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
            list_eliminated_cards_player4, list_players)

def counterattack_player3(random_3,selection_player3,list_situation_player3_counterattack,list_cards_player1,list_cards_player2,
                            list_cards_player3,list_cards_player4,number_players,list_eliminated_cards_player1,
                            list_eliminated_cards_player2,list_eliminated_cards_player3,list_eliminated_cards_player4,list_players):
    #quien contraataca (random_3)
    if random_3 ==1:
        print("Player1 will counterattack player3")
    if random_3 ==2:
        print("Player2 will counterattack player3")
    if number_players ==4 and random_3 ==4:
        print("Player4 will counterattack player3")

    print_challenge()
    #pasar o desafiar contraataque
    selection_player3_2 = int(input("Player3, what do you want to do against the counterattack? Select a option using a number: "))
    #pasar
    if selection_player3_2 == 3:
        print("Player3's action was countered succesfully.")
        situation_player3_counterattack = "lose"
        list_situation_player3_counterattack.append(situation_player3_counterattack)
    #desafiar
    if selection_player3_2 ==1:
        #jugador de turno desafía los contraataquesa los demás
        if random_3 ==1:
            input("player1, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1) + 1):
                    print(str(i)+"-)", list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards.")
            select_counterattack =int(input("Player1 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player1[select_counterattack-1]

        if random_3 ==2:
            input("Player2, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player2) >0:
                for i in range(1,len(list_cards_player2) + 1):
                    print(str(i)+"-)", list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards")
            select_counterattack =int(input("Player2 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player2[select_counterattack-1]

        if random_3 ==4:
            input("Player4, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4) + 1):
                    print(str(i)+"-)", list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards")
            select_counterattack =int(input("Player4 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player4[select_counterattack-1]
        #contraataque  a foreign help:
        if selection_player3 ==2:
            if select_card_counterattack =="Duke":
                print("Player3 was countered succesfully with the card 'Duke'")
                situation_player3_counterattack = "lose"
        
            if select_card_counterattack !="Duke":
                print("The player that counterattacked doesn't have the card 'Duke'")
                situation_player3_counterattack ="win"
        #contraataque al asesino:
        if selection_player3 ==5:
            if select_card_counterattack =="Countess":
                print("Player3 was countered succesfully with the card 'Countess'")
                situation_player3_counterattack = "lose"
        
            if select_card_counterattack !="Countess":
                print("The player that counterattacked doesn't have de card 'Countess'")
                situation_player3_counterattack ="win"
        #contraataque al capitan (steal)
        if selection_player3 ==6:
            if select_card_counterattack =="Ambassador" or select_card_counterattack =="Captain":
                print("Player3 was countered succesfully with the card", select_card_counterattack)
                situation_player3_counterattack = "lose"
        
            else:
                print("The player that counterattacked doesn't have the card 'Captain' or 'Ambassador'")
                situation_player3_counterattack ="win"

        #devolver cartas usadas al maso:
        list_situation_player3_counterattack.append(situation_player3_counterattack)
        if situation_player3_counterattack =="win":
            if random_3 ==1:
                list_eliminated_cards_player1.append(select_card_counterattack)
                list_cards_player1.pop(select_counterattack -1)
            if random_3 ==2:
                list_eliminated_cards_player2.append(select_card_counterattack)
                list_cards_player2.pop(select_counterattack -1)
            if random_3 ==4:
                list_eliminated_cards_player4.append(select_card_counterattack)
                list_cards_player4.pop(select_counterattack -1)

        if situation_player3_counterattack =="lose":
            input("player3, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player3) >0:
                for i in range(1,len(list_cards_player3) + 1):
                    print(str(i)+"-)", list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards")
            select_eliminate =int(input("player3 ,select the card that you prefer to lose, using a number: "))
            eliminate_card = list_cards_player3[select_eliminate-1]
            list_eliminated_cards_player3.append(eliminate_card)
            list_cards_player3.pop(select_eliminate-1)

        life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

    return(list_situation_player3_counterattack,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4, list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
            list_eliminated_cards_player4, list_players)

def counterattack_player4(random_4,selection_player4,list_situation_player4_counterattack,list_cards_player1,list_cards_player2,
                            list_cards_player3,list_cards_player4,number_players,list_eliminated_cards_player1,
                            list_eliminated_cards_player2,list_eliminated_cards_player3,list_eliminated_cards_player4,list_players):
   
  if number_players==4: 
    #quien contraataca (random_4)
    if random_4 ==1:
        print("Player1 will counterattack player4")
    if random_4 ==2:
        print("Player2 will counterattack player4")
    if number_players ==4 and random_4 ==3:
        print("Player3 will counterattack player4")

    print_challenge()
    #pasar o desafiar contraataque
    selection_player4_2 = int(input("Player4, what do you want to do against the counterattack? Select a option using a number: "))
    #pasar
    if selection_player4_2 == 3:
        print("Player4's action was countered succesfully.")
        situation_player4_counterattack = "lose"
        list_situation_player4_counterattack.append(situation_player4_counterattack)
    #desafiar
    if selection_player4_2 ==1:
        #jugador de turno desafía los contraataquesa los demás
        if random_4 ==1:
            input("player1, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1) + 1):
                    print(str(i)+"-)", list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards.")
            select_counterattack =int(input("Player1 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player1[select_counterattack-1]

        if random_4 ==2:
            input("Player2, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player2) >0:
                for i in range(1,len(list_cards_player2) + 1):
                    print(str(i)+"-)", list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards")
            select_counterattack =int(input("Player2 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player2[select_counterattack-1]

        if random_4 ==3:
            input("Player3, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player3) >0:
                for i in range(1,len(list_cards_player3) + 1):
                    print(str(i)+"-)", list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards")
            select_counterattack =int(input("Player3 ,select the card to win the counterattack or lose the card, using a number: "))
            select_card_counterattack =list_cards_player3[select_counterattack-1]
        #contraataque  a foreign help:
        if selection_player4 ==2:
            if select_card_counterattack =="Duke":
                print("Player4 was countered succesfully with the card 'Duke'")
                situation_player4_counterattack = "lose"
        
            if select_card_counterattack !="Duke":
                print("The player that counterattacked doesn't have the card 'Duke'")
                situation_player4_counterattack ="win"
        #contraataque al asesino:
        if selection_player4 ==5:
            if select_card_counterattack =="Countess":
                print("Player4 was countered succesfully with the card 'Countess'")
                situation_player4_counterattack = "lose"
        
            if select_card_counterattack !="Countess":
                print("The player that counterattacked doesn't have de card 'Countess'")
                situation_player4_counterattack ="win"
        #contraataque al capitan (steal)
        if selection_player4 ==6:
            if select_card_counterattack =="Ambassador" or select_card_counterattack =="Captain":
                print("Player4 was countered succesfully with the card", select_card_counterattack)
                situation_player4_counterattack = "lose"
        
            else:
                print("The player that counterattacked doesn't have the card 'Captain' or 'Ambassador'")
                situation_player4_counterattack ="win"

        #devolver cartas usadas al maso:
        list_situation_player4_counterattack.append(situation_player4_counterattack)
        if situation_player4_counterattack =="win":
            if random_4 ==1:
                list_eliminated_cards_player1.append(select_card_counterattack)
                list_cards_player1.pop(select_counterattack -1)
            if random_4 ==2:
                list_eliminated_cards_player2.append(select_card_counterattack)
                list_cards_player2.pop(select_counterattack -1)
            if random_4 ==3:
                list_eliminated_cards_player3.append(select_card_counterattack)
                list_cards_player3.pop(select_counterattack -1)

        if situation_player4_counterattack =="lose":
            input("player4, are you ready to see your cards?, write something when you are ready: ")
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4) + 1):
                    print(str(i)+"-)", list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards")
            select_eliminate =int(input("player4 ,select the card that you prefer to lose, using a number: "))
            eliminate_card = list_cards_player4[select_eliminate-1]
            list_eliminated_cards_player4.append(eliminate_card)
            list_cards_player4.pop(select_eliminate-1)

        life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

    return(list_situation_player4_counterattack,list_cards_player1,list_cards_player2,list_cards_player3,
            list_cards_player4, list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
            list_eliminated_cards_player4, list_players)

def challenge_player1(number_players,random_1,list_cards_player1,list_cards_player2,
                        list_cards_player3, list_cards_player4, selection_player1, list_rest_of_deck,
                        list_eliminated_cards_player1,list_eliminated_cards_player2, 
                        list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player1_challenge):
    print()
    if number_players ==3:
        if random_1 == 2:
            print("Player2 will challenge player1")
        if random_1 == 3:
            print("Player3 will challenge player1")
    
    if number_players ==4:
        print()
        if random_1 == 2:
            print("Player2 will challenge player1")
        if random_1 == 3:
            print("Player3 will challenge player1")
        if random_1 ==4:
            print("Player4 will challenge player1")
            
    print("player1, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player1) >0:
        for i in range(1,len(list_cards_player1)+1):
            print(str(i)+"-)",list_cards_player1[i-1])
    print_space()
    print("player1, scroll up to see your cards.")
    selection_player1_challenge = int(input("player1, select the card to win the challenge or lose the card: "))
    selection_player1_card_challenge = list_cards_player1[selection_player1_challenge-1]

    if selection_player1 ==4:
        print()
        if selection_player1_card_challenge == "Duke":
            print("Player1 has the card 'Duke' and wins the challenge. \n Player1 draws another card from the deck, and loses the card 'Duke'")
            list_rest_of_deck.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            list_cards_player1.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player1_challenge = "win"
        else:
            print("Player1 lost the card",selection_player1_card_challenge)
            list_eliminated_cards_player1.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            situation_player1_challenge = "lose"
                

    if selection_player1 ==5:
        print()
        if selection_player1_card_challenge == "Assassin":
            print("Player1 has the card 'Assassin' and wins the challenge. \n Player1 draws another card from the deck, and loses the card 'Assassin'")
            list_rest_of_deck.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            list_cards_player1.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player1_challenge = "win"
        else:
            print("Player1 lost the card",selection_player1_card_challenge)
            list_eliminated_cards_player1.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            situation_player1_challenge = "lose"
            
    if selection_player1 ==6:
        print()
        if selection_player1_card_challenge == "Captain":
            print("Player1 has the card 'Captain' and wins the challenge. \n Player1 draws another card from the deck, and lose the card 'Captain'")
            list_rest_of_deck.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            list_cards_player1.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player1_challenge = "win"
        else:
            print("Player1 lost the card",selection_player1_card_challenge)
            list_eliminated_cards_player1.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            situation_player1_challenge = "lose"

    if selection_player1 ==7:
        print()
        if selection_player1_card_challenge == "Ambassador":
            print("Player1 has the card 'Ambassador' and wins the challenge. \n Player1 draws another card from the deck, and loses the card 'Ambassador'")
            list_rest_of_deck.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            list_cards_player1.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player1_challenge = "win"
        else:
            print("Player1 lost the card",selection_player1_card_challenge)
            list_eliminated_cards_player1.append(selection_player1_card_challenge)
            list_cards_player1.pop(selection_player1_challenge-1)
            situation_player1_challenge = "lose"
      
    print("Player1, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player1)>0:
        for i in range(1,len(list_cards_player1)+1):
            print(str(i)+"-)",list_cards_player1[i-1])
    print_space()
    print("Player1, scroll up to see your cards.")
    list_situation_player1_challenge.append(situation_player1_challenge)



    if random_1 == 2:
        if situation_player1_challenge == "win":
            print("Player2, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player2) >0:
                for i in range(1,len(list_cards_player2)+1):
                    print(str(i)+"-)",list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards")
            eliminate_card_player2 =int(input("player2, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
            list_cards_player2.pop(eliminate_card_player2-1)
                

    if random_1 == 3:
        if situation_player1_challenge == "win":
            print("Player3, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player3) > 0:
                for i in range(1,len(list_cards_player3)+1):
                    print(str(i)+"-)",list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards.")
            eliminate_card_player3 =int(input("Player3, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
            list_cards_player3.pop(eliminate_card_player3-1)     
            
    if random_1 ==4 and number_players ==4:
        if situation_player1_challenge == "win":
            print("Player4, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4)+1):
                    print(str(i)+"-)",list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards.")
            eliminate_card_player4 =int(input("Player4, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
            list_cards_player4.pop(eliminate_card_player4-1)
        

    return(list_cards_player1, list_cards_player2, list_cards_player3, list_cards_player4,list_eliminated_cards_player1,
            list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player1_challenge)

def challenge_player2(number_players,random_2,list_cards_player1,list_cards_player2,
                        list_cards_player3, list_cards_player4, selection_player2, list_rest_of_deck,
                        list_eliminated_cards_player1,list_eliminated_cards_player2, 
                        list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player2_challenge):
    print()
    if number_players ==3:
        if random_2 == 1:
            print("Player1 will challenge player2")
        if random_2 == 3:
            print("Player3 will challenge player2")
    
    if number_players ==4:
        print()
        if random_2 == 1:
            print("Player1 will challenge player2")
        if random_2 == 3:
            print("Player3 will challenge player2")
        if random_2 ==4:
            print("Player4 will challenge player2")
            
    print("Player2, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player2) >0:
        for i in range(1,len(list_cards_player2)+1):
            print(str(i)+"-)",list_cards_player2[i-1])
    print_space()
    print("Player2, scroll up to see your cards.")
    selection_player2_challenge = int(input("Player2, select the card to win the challenge or lose the card: "))
    selection_player2_card_challenge = list_cards_player2[selection_player2_challenge-1]

    if selection_player2 ==4:
        print()
        if selection_player2_card_challenge == "Duke":
            print("Player2 has the card 'Duke' and wins the challenge. \n Player2 draws another card from the deck, and loses the card 'Duke'")
            list_rest_of_deck.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            list_cards_player2.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player2_challenge = "win"
        else:
            print("Player2 lost the card",selection_player2_card_challenge)
            list_eliminated_cards_player2.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            situation_player2_challenge = "lose"
                

    if selection_player2 ==5:
        print()
        if selection_player2_card_challenge == "Assassin":
            print("Player2 has the card 'Assassin' and wins the challenge. \n Player2 draws another card from the deck, and loses the card 'Assassin'")
            list_rest_of_deck.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            list_cards_player2.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player2_challenge = "win"
        else:
            print("Player2 lost the card",selection_player2_card_challenge)
            list_eliminated_cards_player2.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            situation_player2_challenge = "lose"
            
    if selection_player2 ==6:
        print()
        if selection_player2_card_challenge == "Captain":
            print("Player2 has the card 'Captain' and wins the challenge. \n Player2 draws another card from the deck, and lose the card 'Captain'")
            list_rest_of_deck.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            list_cards_player2.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player2_challenge = "win"
        else:
            print("Player2 lost the card",selection_player2_card_challenge)
            list_eliminated_cards_player2.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            situation_player2_challenge = "lose"

    if selection_player2 ==7:
        print()
        if selection_player2_card_challenge == "Ambassador":
            print("Player2 has the card 'Ambassador' and wins the challenge. \n Player2 draws another card from the deck, and loses the card 'Ambassador'")
            list_rest_of_deck.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            list_cards_player2.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player2_challenge = "win"
        else:
            print("Player2 lost the card",selection_player2_card_challenge)
            list_eliminated_cards_player2.append(selection_player2_card_challenge)
            list_cards_player2.pop(selection_player2_challenge-1)
            situation_player2_challenge = "lose"
      
    print("Player2, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player2)>0:
        for i in range(1,len(list_cards_player2)+1):
            print(str(i)+"-)",list_cards_player2[i-1])
    print_space()
    print("Player2, scroll up to see your cards.")
    list_situation_player2_challenge.append(situation_player2_challenge)



    if random_2 == 1:
        if situation_player2_challenge == "win":
            print("Player1, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1)+1):
                    print(str(i)+"-)",list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards")
            eliminate_card_player1 =int(input("Player1, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
            list_cards_player1.pop(eliminate_card_player1-1)
                

    if random_2 == 3:
        if situation_player2_challenge == "win":
            print("Player3, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player3) > 0:
                for i in range(1,len(list_cards_player3)+1):
                    print(str(i)+"-)",list_cards_player3[i-1])
            print_space()
            print("Player3, scroll up to see your cards.")
            eliminate_card_player3 =int(input("Player3, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
            list_cards_player3.pop(eliminate_card_player3-1)     
            
    if random_2 ==4 and number_players ==4:
        if situation_player2_challenge == "win":
            print("Player4, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4)+1):
                    print(str(i)+"-)",list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards.")
            eliminate_card_player4 =int(input("Player4, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
            list_cards_player4.pop(eliminate_card_player4-1)
        

    return(list_cards_player1, list_cards_player2, list_cards_player3, list_cards_player4,list_eliminated_cards_player1,
            list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player2_challenge)

def challenge_player3(number_players,random_3,list_cards_player1,list_cards_player2,
                        list_cards_player3, list_cards_player4, selection_player3, list_rest_of_deck,
                        list_eliminated_cards_player1,list_eliminated_cards_player2, 
                        list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player3_challenge):
    print()
    if number_players ==3:
        if random_3 == 1:
            print("Player1 will challenge player3")
        if random_3 == 2:
            print("Player2 will challenge player3")
    
    if number_players ==4:
        print()
        if random_3 == 1:
            print("Player1 will challenge player3")
        if random_3 == 3:
            print("Player2 will challenge player3")
        if random_3 ==4:
            print("Player4 will challenge player3")
            
    print("Player3, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player3) >0:
        for i in range(1,len(list_cards_player3)+1):
            print(str(i)+"-)",list_cards_player3[i-1])
    print_space()
    print("Player3, scroll up to see your cards.")
    selection_player3_challenge = int(input("Player3, select the card to win the challenge or lose the card: "))
    selection_player3_card_challenge = list_cards_player3[selection_player3_challenge-1]

    if selection_player3 ==4:
        print()
        if selection_player3_card_challenge == "Duke":
            print("Player3 has the card 'Duke' and wins the challenge. \n Player3 draws another card from the deck, and loses the card 'Duke'")
            list_rest_of_deck.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            list_cards_player3.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player3_challenge = "win"
        else:
            print("Player3 lost the card",selection_player3_card_challenge)
            list_eliminated_cards_player3.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            situation_player3_challenge = "lose"
                

    if selection_player3 ==5:
        print()
        if selection_player3_card_challenge == "Assassin":
            print("Player3 has the card 'Assassin' and wins the challenge. \n Player3 draws another card from the deck, and loses the card 'Assassin'")
            list_rest_of_deck.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            list_cards_player3.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player3_challenge = "win"
        else:
            print("Player3 lost the card",selection_player3_card_challenge)
            list_eliminated_cards_player3.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            situation_player3_challenge = "lose"
            
    if selection_player3 ==6:
        print()
        if selection_player3_card_challenge == "Captain":
            print("Player3 has the card 'Captain' and wins the challenge. \n Player3 draws another card from the deck, and lose the card 'Captain'")
            list_rest_of_deck.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            list_cards_player3.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player3_challenge = "win"
        else:
            print("Player3 lost the card",selection_player3_card_challenge)
            list_eliminated_cards_player3.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            situation_player3_challenge = "lose"

    if selection_player3 ==7:
        print()
        if selection_player3_card_challenge == "Ambassador":
            print("Player3 has the card 'Ambassador' and wins the challenge. \n Player3 draws another card from the deck, and loses the card 'Ambassador'")
            list_rest_of_deck.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            list_cards_player3.append(list_rest_of_deck[0])
            list_rest_of_deck.pop(0)
            situation_player3_challenge = "win"
        else:
            print("Player3 lost the card",selection_player3_card_challenge)
            list_eliminated_cards_player3.append(selection_player3_card_challenge)
            list_cards_player3.pop(selection_player3_challenge-1)
            situation_player3_challenge = "lose"
      
    print("Player3, Are you ready to see your cards?")
    input("Write something when you are ready: ")
    print()
    print()
    if len(list_cards_player3)>0:
        for i in range(1,len(list_cards_player3)+1):
            print(str(i)+"-)",list_cards_player3[i-1])
    print_space()
    print("Player3, scroll up to see your cards.")
    list_situation_player3_challenge.append(situation_player3_challenge)



    if random_3 == 1:
        if situation_player3_challenge == "win":
            print("Player1, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player1) >0:
                for i in range(1,len(list_cards_player1)+1):
                    print(str(i)+"-)",list_cards_player1[i-1])
            print_space()
            print("Player1, scroll up to see your cards")
            eliminate_card_player1 =int(input("Player1, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
            list_cards_player1.pop(eliminate_card_player1-1)
                

    if random_3 == 2:
        if situation_player3_challenge == "win":
            print("Player2, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player2) > 0:
                for i in range(1,len(list_cards_player2)+1):
                    print(str(i)+"-)",list_cards_player2[i-1])
            print_space()
            print("Player2, scroll up to see your cards.")
            eliminate_card_player2 =int(input("Player2, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
            list_cards_player2.pop(eliminate_card_player2-1)     
            
    if random_3 ==4 and number_players ==4:
        if situation_player3_challenge == "win":
            print("Player4, are you ready to see your cards?")
            input("Write something when you are ready: ")
            print()
            print()
            if len(list_cards_player4) >0:
                for i in range(1,len(list_cards_player4)+1):
                    print(str(i)+"-)",list_cards_player4[i-1])
            print_space()
            print("Player4, scroll up to see your cards.")
            eliminate_card_player4 =int(input("Player4, select the card that you prefer to lose, using a number : "))
            list_eliminated_cards_player4.append(list_cards_player4[eliminate_card_player4-1])
            list_cards_player4.pop(eliminate_card_player4-1)
        

    return(list_cards_player1, list_cards_player2, list_cards_player3, list_cards_player4,list_eliminated_cards_player1,
            list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player3_challenge)

def challenge_player4(number_players,random_4,list_cards_player1,list_cards_player2,
                        list_cards_player3, list_cards_player4, selection_player4, list_rest_of_deck,
                        list_eliminated_cards_player1,list_eliminated_cards_player2, 
                        list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player4_challenge):

    if number_players ==4:
        print()
        if random_4 == 1:
            print("Player1 will challenge player4")
        if random_4 == 2:
            print("Player2 will challenge player4")
        if random_4 ==3:
            print("Player3 will challenge player4")
            
        print("Player4, are you ready to see your cards?")
        input("Write something when you are ready: ")
        print()
        print()
        if len(list_cards_player4) >0:
            for i in range(1,len(list_cards_player4)+1):
                print(str(i)+"-)",list_cards_player4[i-1])
        print_space()
        print("Player4, scroll up to see your cards.")
        selection_player4_challenge = int(input("Player4, select the card to win the challenge or lose the card: "))
        selection_player4_card_challenge = list_cards_player4[selection_player4_challenge-1]

        if selection_player4 ==4:
            print()
            if selection_player4_card_challenge == "Duke":
                print("Player4 has the card 'Duke' and wins the challenge. \n Player4 draws another card from the deck, and loses the card 'Duke'")
                list_rest_of_deck.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                list_cards_player4.append(list_rest_of_deck[0])
                list_rest_of_deck.pop(0)
                situation_player4_challenge = "win"
            else:
                print("Player4 lost the card",selection_player4_card_challenge)
                list_eliminated_cards_player4.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                situation_player4_challenge = "lose"
                

        if selection_player4 ==5:
            print()
            if selection_player4_card_challenge == "Assassin":
                print("Player4 has the card 'Assassin' and wins the challenge. \n Player4 draws another card from the deck, and loses the card 'Assassin'")
                list_rest_of_deck.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                list_cards_player4.append(list_rest_of_deck[0])
                list_rest_of_deck.pop(0)
                situation_player4_challenge = "win"
            else:
                print("Player4 lost the card",selection_player4_card_challenge)
                list_eliminated_cards_player4.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                situation_player4_challenge = "lose"
            
        if selection_player4 ==6:
            print()
            if selection_player4_card_challenge == "Captain":
                print("Player4 has the card 'Captain' and wins the challenge. \n Player4 draws another card from the deck, and lose the card 'Captain'")
                list_rest_of_deck.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                list_cards_player4.append(list_rest_of_deck[0])
                list_rest_of_deck.pop(0)
                situation_player4_challenge = "win"
            else:
                print("Player4 lost the card",selection_player4_card_challenge)
                list_eliminated_cards_player4.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                situation_player4_challenge = "lose"

        if selection_player4 ==7:
            print()
            if selection_player4_card_challenge == "Ambassador":
                print("Player4 has the card 'Ambassador' and wins the challenge. \n Player4 draws another card from the deck, and loses the card 'Ambassador'")
                list_rest_of_deck.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                list_cards_player4.append(list_rest_of_deck[0])
                list_rest_of_deck.pop(0)
                situation_player4_challenge = "win"
            else:
                print("Player4 lost the card",selection_player4_card_challenge)
                list_eliminated_cards_player4.append(selection_player4_card_challenge)
                list_cards_player4.pop(selection_player4_challenge-1)
                situation_player4_challenge = "lose"
      
        print("Player4, Are you ready to see your cards?")
        input("Write something when you are ready: ")
        print()
        print()
        if len(list_cards_player4)>0:
            for i in range(1,len(list_cards_player4)+1):
                print(str(i)+"-)",list_cards_player4[i-1])
        print_space()
        print("Player4, scroll up to see your cards.")
        list_situation_player4_challenge.append(situation_player4_challenge)



        if random_4 == 1:
            if situation_player4_challenge == "win":
                print("Player1, are you ready to see your cards?")
                input("Write something when you are ready: ")
                print()
                print()
                if len(list_cards_player1) >0:
                    for i in range(1,len(list_cards_player1)+1):
                        print(str(i)+"-)",list_cards_player1[i-1])
                print_space()
                print("Player1, scroll up to see your cards")
                eliminate_card_player1 =int(input("Player1, select the card that you prefer to lose, using a number : "))
                list_eliminated_cards_player1.append(list_cards_player1[eliminate_card_player1-1])
                list_cards_player1.pop(eliminate_card_player1-1)
                

        if random_4 == 2:
            if situation_player3_challenge == "win":
                print("Player2, are you ready to see your cards?")
                input("Write something when you are ready: ")
                print()
                print()
                if len(list_cards_player2) > 0:
                    for i in range(1,len(list_cards_player2)+1):
                        print(str(i)+"-)",list_cards_player2[i-1])
                print_space()
                print("Player2, scroll up to see your cards.")
                eliminate_card_player2 =int(input("Player2, select the card that you prefer to lose, using a number : "))
                list_eliminated_cards_player2.append(list_cards_player2[eliminate_card_player2-1])
                list_cards_player2.pop(eliminate_card_player2-1)     
            
        if random_4 ==3:
            if situation_player4_challenge == "win":
                print("Player3, are you ready to see your cards?")
                input("Write something when you are ready: ")
                print()
                print()
                if len(list_cards_player3) >0:
                    for i in range(1,len(list_cards_player3)+1):
                        print(str(i)+"-)",list_cards_player3[i-1])
                print_space()
                print("Player3, scroll up to see your cards.")
                eliminate_card_player3 =int(input("Player3, select the card that you prefer to lose, using a number : "))
                list_eliminated_cards_player3.append(list_cards_player3[eliminate_card_player3-1])
                list_cards_player3.pop(eliminate_card_player3-1)
        

    return(list_cards_player1, list_cards_player2, list_cards_player3, list_cards_player4,list_eliminated_cards_player1,
            list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player4_challenge)



def game_player4(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4):
    list_all_actions = ["income","foreign help","Coup","Duke-Taxes","Assassin-Assassination",
                                   "Captain-Extortion", "Ambassador-Change"]
    i = 0
    while True:

 
            
        if list_players[3].live_game =="yes":
            
            if list_players[3].coins_game < 10:
                print_actions()
                print()
                selection_player4 = int(input("Player4, it's your turn. Choose an action using a number: "))
                print()

                #estas son las funciones de la seleccion del player4
                #coup:
                if selection_player4 ==3:
                    if list_players[3].coins_game -7 >= 0:
                        list_players[3].coins_game -=7
                        player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                        list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                        list_eliminated_cards_player3, list_eliminated_cards_player4)
                    else:
                        while True:
                            selection_player4 = int(input("Player4, you dont have the coins for this action. \nSelect another action, using a number: "))
                            if selection_player4 !=3 :
                                break
                #asesino
                if selection_player4 ==5:
                    if list_players[3].coins_game -3 >= 0:
                        list_players[3].coins_game -= 3
                        print_challenge_or_counterattack()
                    else:
                        while True:
                            selection_player4 = int(input("player4, you dont have the coins for this action, \nSelect other action, using a number: "))
                            if selection_player4 != 5 and selection_player4 != 3:
                                break
                
                #income:
                if selection_player4 == 1:
                    list_players[3].coins_game += 1
                    print("A coin has been added to player4")
                    print()
                    print_coins_players(list_players)

                    
                
                #capitan(steal):          
                if selection_player4 ==6:
                    print_challenge_or_counterattack()
                #foreign aid:
                if selection_player4 == 2:
                    print_counterattack()
                #duke/ambassador
                if selection_player4 == 4 or selection_player4 ==7:
                    print_challenge()

                

                #aqui parte los desafios o contraataques para el player4

                if selection_player4 != 1 and selection_player4 !=3:
                    if list_players[0].live_game == "yes":
                        selection_player1 =int(input("Player1, choose an option using a number: "))
                    else:
                        selection_player1 = 0
                    if list_players[1].live_game == "yes":
                        selection_player2 =int(input("Player2, choose a option using a number: "))
                    else: 
                        selection_player2 = 0
                    
                    if list_players[2].live_game =="yes":
                            selection_player3 = int(input("Player3, choose a option using a number: "))
                    else:
                            selection_player3 = 0

                    #esta la parte del desafio
                    situation_player4_challenge =""
                    situation_player4_counterattack =""
                    
                    if number_players == 4:
                        #esta es la parte del desafio para 4 jugadores en el turno del jugador4
                        if (selection_player1 == 1 or selection_player2 == 1 or selection_player3==1) and (selection_player4==4 or selection_player4 ==5
                            or selection_player4 ==6 or selection_player4==7):
                            
                            if selection_player1 ==1 and selection_player2 !=1 and selection_player3 !=1:
                                random_4 = 1
                            elif selection_player1 !=1 and selection_player2 ==1 and selection_player3 !=1:
                                random_4 =2
                            elif selection_player1 !=1 and selection_player2 !=1 and selection_player3 ==1:
                                random_4 =3
                            elif selection_player1 ==1 and selection_player2 ==1 and selection_player3 !=1:
                                print("Whoever challenges player4, will be chosen at random")
                                random_4 = random.randint(1,2)
                        
                            elif selection_player1 ==1 and selection_player2 !=1 and selection_player3 ==1:
                                print("Whoever challenges player4, will be chosen at random")
                                random_4 = random.randint(1,2)
                                if random_4 ==2:
                                    random_4 =3
    
                            elif selection_player1 !=1 and selection_player2 ==1 and selection_player3 ==1:
                                print("Whoever challenges player4, will be chosen at random")
                                random_4 = random.randint(2,3)
                                
                            elif selection_player1 ==1 and selection_player2 ==1 and selection_player3 ==1:
                                print("Whoever challenges player4, will be chosen at random")
                                random_4 =random.randint(1,3)
                                
                            list_situation_player4_challenge =[]
                            challenge_player4(number_players,random_4,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player3, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player4_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player4_challenge = list_situation_player4_challenge[0]
                            list_situation_player4_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)


                        #esta es la parte del contraattaque para 4 jugadores en el turno del player3
                        if (selection_player1 ==2 or selection_player2 ==2 or selection_player3 ==2 ) and (selection_player4 ==2 or 
                            selection_player4 ==5 or selection_player4 ==6) and situation_player4_challenge != "lose":
                                print("Counterattack!")
                                if selection_player1 ==2 and selection_player2 !=2 and selection_player3 !=2:
                                    random_4 =1
                                if selection_player1 !=2 and selection_player2 ==2 and selection_player3 !=2:
                                    random_4 =2
                                if selection_player1 !=2 and selection_player2 !=2 and selection_player3 ==2:
                                    random_4 =3
                                if selection_player1 ==2 and selection_player2 ==2 and selection_player3 !=2:
                                    print("Whoever counterattacks player4, will be chosen at random")
                                    random_4 =random.randint(1,2)
                                    
                                if selection_player1 ==2 and selection_player2 !=2 and selection_player3 ==2:
                                    print("Whoever counterattacks player4, will be chosen at random")
                                    random_4 =random.randint(1,2)
                                    if random_4 ==2:
                                        random_4 = 3
                                    
                                if selection_player1 !=2 and selection_player2 ==2 and selection_player3 ==2:
                                    print("Whoever counterattacks player4, will be chosen at random")
                                    random_4 =random.randint(2,3)
                                   
                                if selection_player1 ==2 and selection_player2 ==2 and selection_player3 ==2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_4 =random.randint(1,3)
                                    

                                list_situation_player4_counterattack = []
                                counterattack_player4(random_4,selection_player4,list_situation_player4_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)
                                                    
                                situation_player4_counterattack = list_situation_player4_counterattack[0]
                                list_situation_player4_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    #aca se ven las acciones del player4 despues de los desafios o contraataques, hay que revisarlo
                    
                    if situation_player4_challenge == "win" and situation_player4_counterattack =="win":
                        player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player4_challenge =="win" and situation_player4_counterattack =="":
                        player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player4_challenge =="" and situation_player4_counterattack =="win":
                        player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player4_challenge =="" and situation_player4_counterattack =="":
                        player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
                    
                    if selection_player4 ==5 and situation_player4_challenge =="lose":
                        list_players[3].coins_game +=3

            elif list_players[3].coins_game >= 10:
                selection_player4 = 3
                list_players[3].coins_game -=7
                player4_actions(selection_player4,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)

       
        
    
         #aqui inicia el turno del player1
        if list_players[0].live_game =="yes":
            print("It's player1's turn")
            game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            print("Player1 is no longer in the game")
        #aqui inicia el turno del player2
        if list_players[1].live_game =="yes":
            print("It's player2's turn:")
            game_player2(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            print("Player2 is no longer in the game")
        #aqui inicia el turno del player3
        if list_players[2].live_game =="yes":
                print("It's player3's turn:")
                game_player3(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            sys.exit("Player4 has won the game!")
            

def game_player3(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4):
    list_all_actions = ["income","foreign help","Coup","Duke-Taxes","Assassin-Assassination",
                                   "Captain-Extortion", "Ambassador-Change"]
    i = 0
    while True:

        #sigue vivo el player3?:
            
        if list_players[2].live_game =="yes":
            
            if list_players[2].coins_game < 10:
                print_actions()
                print()
                selection_player3 = int(input("Player3, it's your turn. Choose an action using a number: "))
                print()

                #estas son las funciones de la seleccion del player3
                #coup:
                if selection_player3 ==3:
                    if list_players[2].coins_game -7 >= 0:
                        list_players[2].coins_game -=7
                        player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                        list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                        list_eliminated_cards_player3, list_eliminated_cards_player4)
                    else:
                        while True:
                            selection_player3 = int(input("Player3, you dont have the coins for this action. \nSelect another action, using a number: "))
                            if selection_player3 !=3 :
                                break
                #asesino
                if selection_player3 ==5:
                    if list_players[2].coins_game -3 >= 0:
                        list_players[2].coins_game -= 3
                        print_challenge_or_counterattack()
                    else:
                        while True:
                            selection_player3 = int(input("player3, you dont have the coins for this action, \nSelect other action, using a number: "))
                            if selection_player3 != 5 and selection_player3 != 3:
                                break
                
                #income:
                if selection_player3 == 1:
                    list_players[2].coins_game += 1
                    print("A coin has been added to player3")
                    print()
                    print_coins_players(list_players)

                    
                
                #capitan(steal):          
                if selection_player3 ==6:
                    print_challenge_or_counterattack()
                #foreign aid:
                if selection_player3 == 2:
                    print_counterattack()
                #duke/ambassador
                if selection_player3 == 4 or selection_player3 ==7:
                    print_challenge()

                

                #aqui parte los desafios o contraataques para el player3

                if selection_player3 != 1 and selection_player3 !=3:
                    if list_players[0].live_game == "yes":
                        selection_player1 =int(input("Player1, choose an option using a number: "))
                    else:
                        selection_player1 = 0
                    if list_players[1].live_game == "yes":
                        selection_player2 =int(input("Player2, choose a option using a number: "))
                    else: 
                        selection_player2 = 0
                    if number_players ==4:
                        if list_players[3].live_game =="yes":
                            selection_player4 = int(input("Player4, choose a option using a number: "))
                        else:
                            selection_player4 = 0

                    #esta la parte del desafio
                    situation_player3_challenge =""
                    situation_player3_counterattack =""
                    if number_players ==3:
                        #esta es la parte del desafio para 3 jugadores en el turno del jugador3
                        #si algun player (no el de turno) elige 1(challenge)
                        #y player3 elige algo que se puede desafiar:
                        if (selection_player1 == 1 or selection_player2 == 1) and (selection_player3==4 or selection_player3==5
                            or selection_player3 ==6 or selection_player3==7):

                            print()
                            #si los dos desafían:
                            if selection_player1 ==1 and selection_player2 ==1:
                                print("Whoever challenges player3, will be chosen at random.")
                                random_3 = random.randint(1,2)
                            
                            #si no desafían ambos:
                            elif selection_player1 ==1 and selection_player2 !=1:
                                random_3 =1
                            elif selection_player1 !=1 and selection_player2 ==1:
                                random_3 = 2
                            list_situation_player3_challenge =[]
                            challenge_player3(number_players,random_3,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player3, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player3_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player3_challenge =list_situation_player3_challenge[0]
                            list_situation_player3_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                        #aqui comienza el contraatque para el jugador3
                        if (selection_player1 ==2 or selection_player2 ==2) and (selection_player3 ==2 or selection_player3 ==5 or 
                                selection_player3 ==6) and situation_player3_challenge != "lose":
                                
                                if selection_player1 ==2 and selection_player2 !=2:
                                    random_3 =1
                                if selection_player1 !=2 and selection_player2 ==2:
                                    random_3 =2
                                if selection_player1 ==2 and selection_player2 ==2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_3 =random.randint(1,2)
                                

                                list_situation_player3_counterattack = []
                                counterattack_player3(random_3,selection_player3,list_situation_player3_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)

                                situation_player3_counterattack = list_situation_player3_counterattack[0]
                                list_situation_player3_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    if number_players == 4:
                        #esta es la parte del desafio para 4 jugadores en el turno del jugador3
                        if (selection_player1 == 1 or selection_player2 == 1 or selection_player4==1) and (selection_player3==4 or selection_player3 ==5
                            or selection_player3 ==6 or selection_player3==7):
                            
                            if selection_player1 ==1 and selection_player2 !=1 and selection_player4 !=1:
                                random_3 = 1
                            elif selection_player1 !=1 and selection_player2 ==1 and selection_player4 !=1:
                                random_3 =2
                            elif selection_player1 !=1 and selection_player2 !=1 and selection_player4 ==1:
                                random_3 =4
                            elif selection_player1 ==1 and selection_player2 ==1 and selection_player4 !=1:
                                print("Whoever challenges player3, will be chosen at random")
                                random_3 = random.randint(1,2)
                        
                            elif selection_player1 ==1 and selection_player2 !=1 and selection_player4 ==1:
                                print("Whoever challenges player3, will be chosen at random")
                                random_3 = random.randint(1,2)
                                if random_3 ==2:
                                    random_3 =4
    
                            elif selection_player1 !=1 and selection_player2 ==1 and selection_player4 ==1:
                                print("Whoever challenges player3, will be chosen at random")
                                random_3 = random.randint(3,4)
                                if random_3==3:
                                    random_3=1
                            elif selection_player1 ==1 and selection_player2 ==1 and selection_player4 ==1:
                                print("Whoever challenges player3, will be chosen at random")
                                random_3 =random.randint(2,4)
                                if random_3==3:
                                    random_3=1
                            list_situation_player3_challenge =[]
                            challenge_player3(number_players,random_3,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player3, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player3_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player3_challenge = list_situation_player3_challenge[0]
                            list_situation_player3_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)


                        #esta es la parte del contraattaque para 4 jugadores en el turno del player3
                        if (selection_player1 ==2 or selection_player2 ==2 or selection_player4 ==2 ) and (selection_player3 ==2 or 
                            selection_player3 ==5 or selection_player3 ==6) and situation_player3_challenge != "lose":
                                print("Counterattack!")
                                if selection_player1 ==2 and selection_player2 !=2 and selection_player4 !=2:
                                    random_3 =1
                                if selection_player1 !=2 and selection_player2 ==2 and selection_player4 !=2:
                                    random_3 =2
                                if selection_player1 !=2 and selection_player2 !=2 and selection_player4 ==2:
                                    random_3 =4
                                if selection_player1 ==2 and selection_player2 ==2 and selection_player4 !=2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_3 =random.randint(1,2)
                                    
                                if selection_player1 ==2 and selection_player2 !=2 and selection_player4 ==2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_3 =random.randint(1,2)
                                    if random_3 ==2:
                                        random_3 = 4
                                    
                                if selection_player1 !=2 and selection_player2 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_3 =random.randint(3,4)
                                    if random_3==3:
                                        random_3=2

                                if selection_player1 ==2 and selection_player2 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player3, will be chosen at random")
                                    random_3 =random.randint(1,3)
                                    if random_3==3:
                                        random_3=4

                                list_situation_player3_counterattack = []
                                counterattack_player3(random_3,selection_player3,list_situation_player3_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)
                                                    
                                situation_player3_counterattack = list_situation_player3_counterattack[0]
                                list_situation_player3_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    #aca se ven las acciones del player3 despues de los desafios o contra_ataques, hay que revisarlo
                    
                    if situation_player3_challenge == "win" and situation_player3_counterattack =="win":
                        player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player3_challenge =="win" and situation_player3_counterattack =="":
                        player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player3_challenge =="" and situation_player3_counterattack =="win":
                        player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player3_challenge =="" and situation_player3_counterattack =="":
                        player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
                    
                    if selection_player3 ==5 and situation_player3_challenge =="lose":
                        list_players[2].coins_game +=3

            elif list_players[2].coins_game >= 10:
                selection_player3 = 3
                list_players[2].coins_game -=7
                player3_actions(selection_player3,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)

       
        
        #aqui inicia el turno del player4
        if  number_players ==4:
            if list_players[3].live_game =="yes":
                print("It's Player4's turn:")
                game_player4(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
            else:
                print("Player4 is no longer in the game")
         #aqui inicia el turno del player1
        if list_players[0].live_game =="yes":
            print("It's player1's turn")
            game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            print("Player1 is no longer in the game")
        #aqui inicia el turno del player2
        if list_players[1].live_game =="yes":
            print("It's player2's turn:")
            game_player2(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            sys.exit("Player3 has won the game!")
            

def game_player2(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4):
    list_all_actions = ["income","foreign help","Coup","Duke-Taxes","Assassin-Assassination",
                                   "Captain-Extortion", "Ambassador-Change"]
    i = 0
    while True:

        #sigue vivo el player2?:
            
        if list_players[1].live_game =="yes":
            
            if list_players[1].coins_game < 10:
                print_actions()
                print()
                selection_player2 = int(input("Player2, it's your turn. Choose an action using a number: "))
                print()

                #estas son las funciones de la seleccion del player2
                #coup:
                if selection_player2 ==3:
                    if list_players[1].coins_game -7 >= 0:
                        list_players[1].coins_game -=7
                        player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                        list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                        list_eliminated_cards_player3, list_eliminated_cards_player4)
                    else:
                        while True:
                            selection_player2 = int(input("Player2, you dont have the coins for this action. \nSelect another action, using a number: "))
                            if selection_player2 !=3 :
                                break
                #asesino
                if selection_player2 ==5:
                    if list_players[1].coins_game -3 >= 0:
                        list_players[1].coins_game -= 3
                        print_challenge_or_counterattack()
                    else:
                        while True:
                            selection_player2 = int(input("player2, you dont have the coins for this action, \nSelect other action, using a number: "))
                            if selection_player2 != 5 and selection_player2 != 3:
                                break
                
                #income:
                if selection_player2 == 1:
                    list_players[1].coins_game += 1
                    print("A coin has been added to player2")
                    print()
                    print_coins_players(list_players)

                    
                
                #capitan(steal):          
                if selection_player2 ==6:
                    print_challenge_or_counterattack()
                #foreign aid:
                if selection_player2 == 2:
                    print_counterattack()
                #duke/ambassador
                if selection_player2 == 4 or selection_player2 ==7:
                    print_challenge()

                

                #aqui parte los desafios o contraataques para el player2

                if selection_player2 != 1 and selection_player2 !=3:
                    if list_players[0].live_game == "yes":
                        selection_player1 =int(input("Player1, choose an option using a number: "))
                    else:
                        selection_player1 = 0
                    if list_players[2].live_game == "yes":
                        selection_player3 =int(input("Player3, choose a option using a number: "))
                    else: 
                        selection_player3 = 0
                    if number_players ==4:
                        if list_players[3].live_game =="yes":
                            selection_player4 = int(input("Player4, choose a option using a number: "))
                        else:
                            selection_player4 = 0

                    #esta la parte del desafio
                    situation_player2_challenge =""
                    situation_player2_counterattack =""
                    if number_players ==3:
                        #esta es la parte del desafio para 3 jugadores en el turno del jugador1
                        #si algun player (no el de turno) elige 1(challenge)
                        #y player1 elige algo que se puede desafiar:
                        if (selection_player1 == 1 or selection_player3 == 1) and (selection_player2==4 or selection_player2==5
                            or selection_player2 ==6 or selection_player2==7):

                            print()
                            #si los dos desafían:
                            if selection_player1 ==1 and selection_player3 ==1:
                                print("Whoever challenges player2, will be chosen at random.")
                                random_2 = random.randint(2,3)
                                if random_2 == 2:
                                    random_2 = 1
                            #si no desafían ambos:
                            elif selection_player1 ==1 and selection_player3 !=1:
                                random_2 =1
                            elif selection_player1 !=1 and selection_player3 ==1:
                                random_2 = 3
                            list_situation_player2_challenge =[]
                            challenge_player2(number_players,random_2,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player2, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player2_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player2_challenge =list_situation_player2_challenge[0]
                            list_situation_player2_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                        #aqui comienza el contraatque para el jugador2
                        if (selection_player1 ==2 or selection_player3 ==2) and (selection_player2 ==2 or selection_player2 ==5 or 
                                selection_player2 ==6) and situation_player2_challenge != "lose":
                                
                                if selection_player1 ==2 and selection_player3 !=2:
                                    random_2 =1
                                if selection_player1 !=2 and selection_player3 ==2:
                                    random_2 =3
                                if selection_player1 ==2 and selection_player3 ==2:
                                    print("Whoever counterattacks player2, will be chosen at random")
                                    random_2 =random.randint(2,3)
                                    if random_2==2:
                                        random_2 =1

                                list_situation_player2_counterattack = []
                                counterattack_player2(random_2,selection_player2,list_situation_player2_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)

                                situation_player2_counterattack = list_situation_player2_counterattack[0]
                                list_situation_player2_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    if number_players == 4:
                        #esta es la parte del desafio para 4 jugadores en el turno del jugador2
                        if (selection_player1 == 1 or selection_player3 == 1 or selection_player4==1) and (selection_player2==4 or selection_player2 ==5
                            or selection_player2 ==6 or selection_player2==7):
                            
                            if selection_player1 ==1 and selection_player3 !=1 and selection_player4 !=1:
                                random_2 = 1
                            elif selection_player1 !=1 and selection_player3 ==1 and selection_player4 !=1:
                                random_2 =3
                            elif selection_player1 !=1 and selection_player3 !=1 and selection_player4 ==1:
                                random_2 =4
                            elif selection_player1 ==1 and selection_player3 ==1 and selection_player4 !=1:
                                print("Whoever challenges player2, will be chosen at random")
                                random_2 = random.randint(2,3)
                                if random_2==2:
                                    random_2 =1
                            elif selection_player1 ==1 and selection_player3 !=1 and selection_player4 ==1:
                                print("Whoever challenges player2, will be chosen at random")
                                random_2 = random.randint(1,2)
                                if random_2 ==2:
                                    random_2 =4
    
                            elif selection_player1 !=1 and selection_player3 ==1 and selection_player4 ==1:
                                print("Whoever challenges player2, will be chosen at random")
                                random_2 = random.randint(3,4)
                            elif selection_player1 ==1 and selection_player3 ==1 and selection_player4 ==1:
                                print("Whoever challenges player2, will be chosen at random")
                                random_2 =random.randint(2,4)
                                if random_2==2:
                                    random_2=1
                            list_situation_player2_challenge =[]
                            challenge_player2(number_players,random_2,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player2, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player2_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player2_challenge = list_situation_player2_challenge[0]
                            list_situation_player2_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)


                        #esta es la parte del contraattaque para 4 jugadores en el turno del player2
                        if (selection_player1 ==2 or selection_player3 ==2 or selection_player4 ==2 ) and (selection_player2 ==2 or 
                            selection_player2 ==5 or selection_player2 ==6) and situation_player2_challenge != "lose":
                                print("Counterattack!")
                                if selection_player1 ==2 and selection_player3 !=2 and selection_player4 !=2:
                                    random_2 =1
                                if selection_player1 !=2 and selection_player3 ==2 and selection_player4 !=2:
                                    random_2 =3
                                if selection_player1 !=2 and selection_player3 !=2 and selection_player4 ==2:
                                    random_2 =4
                                if selection_player1 ==2 and selection_player3 ==2 and selection_player4 !=2:
                                    print("Whoever counterattacks player2, will be chosen at random")
                                    random_2 =random.randint(2,3)
                                    if random_2==2:
                                        random_2=1
                                if selection_player1 ==2 and selection_player3 !=2 and selection_player4 ==2:
                                    print("Whoever counterattacks player2, will be chosen at random")
                                    random_2 =random.randint(1,2)
                                    if random_2 ==2:
                                        random_2 = 4
                                    
                                if selection_player1 !=2 and selection_player3 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player2, will be chosen at random")
                                    random_2 =random.randint(3,4)

                                if selection_player1 ==2 and selection_player3 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player2, will be chosen at random")
                                    random_2 =random.randint(2,4)
                                    if random_2==2:
                                        random_2=1

                                list_situation_player2_counterattack = []
                                counterattack_player2(random_2,selection_player2,list_situation_player2_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)
                                                    
                                situation_player2_counterattack = list_situation_player2_counterattack[0]
                                list_situation_player2_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    #aca se ven las acciones del player2 despues de los desafios o contra_ataques, hay que revisarlo
                    
                    if situation_player2_challenge == "win" and situation_player2_counterattack =="win":
                        player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player2_challenge =="win" and situation_player2_counterattack =="":
                        player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player2_challenge =="" and situation_player2_counterattack =="win":
                        player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player2_challenge =="" and situation_player2_counterattack =="":
                        player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
                    
                    if selection_player2 ==5 and situation_player2_challenge =="lose":
                        list_players[1].coins_game +=3

            elif list_players[1].coins_game >= 10:
                selection_player2 = 3
                list_players[1].coins_game -=7
                player2_actions(selection_player2,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)

       
        #aqui inicia el turno del player3
        if list_players[2].live_game =="yes":
            print("Player3, it's your turn:")
            game_player3(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else: 
            print("Player3 is no longer in the game")
        #aqui inicia el turno del player4
        if  number_players ==4:
            if list_players[3].live_game =="yes":
                print("Player4 it's your turn:")
                game_player4(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
            else:
                print("Player4 is no longer in the game")
         #aqui inicia el turno del player1
        if list_players[0].live_game =="yes":
            print("Player1, it's your turn:")
            game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        
        else:
            sys.exit("Player2 has won the game!")
           

def game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4):

    list_all_actions = ["income","foreign help","Coup","Duke-Taxes","Assassin-Assassination",
                                   "Captain-Extortion", "Ambassador-Change"]
    i = 0
    while True:

        #sigue vivo el player1?:
            
        if list_players[0].live_game =="yes":
            
            if list_players[0].coins_game < 10:
                print_actions()
                print()
                selection_player1 = int(input("Player1, it's your turn. Choose an action using a number: "))
                print()

                #estas son las funciones de la seleccion del player1
                #coup:
                if selection_player1 ==3:
                    if list_players[0].coins_game -7 >= 0:
                        list_players[0].coins_game -=7
                        player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                        list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                        list_eliminated_cards_player3, list_eliminated_cards_player4)
                    else:
                        while True:
                            selection_player1 = int(input("Player1, you dont have the coins for this action. \nSelect another action, using a number: "))
                            if selection_player1 !=3 :
                                break
                #asesino
                if selection_player1 ==5:
                    if list_players[0].coins_game -3 >= 0:
                        list_players[0].coins_game -= 3
                        print_challenge_or_counterattack()
                    else:
                        while True:
                            selection_player1 = int(input("player1, you dont have the coins for this action, \nSelect other action, using a number: "))
                            if selection_player1 != 5 and selection_player1 != 3:
                                break
                
                #income:
                if selection_player1 == 1:
                    list_players[0].coins_game += 1
                    print("A coin has been added to player1")
                    print()
                    print_coins_players(list_players)

                    
                
                #capitan(steal):          
                if selection_player1 ==6:
                    print_challenge_or_counterattack()
                #foreign aid:
                if selection_player1 == 2:
                    print_counterattack()
                #duke/ambassador
                if selection_player1 == 4 or selection_player1 ==7:
                    print_challenge()

                

                #aqui parte los desafios o contraataques para el player1

                if selection_player1 != 1 and selection_player1 !=3:
                    if list_players[1].live_game == "yes":
                        selection_player2 =int(input("Player2, choose an option using a number: "))
                    else:
                        selection_player2 = 0
                    if list_players[2].live_game == "yes":
                        selection_player3 =int(input("Player3, choose a option using a number: "))
                    else: 
                        selection_player3 = 0
                    if number_players ==4:
                        if list_players[3].live_game =="yes":
                            selection_player4 = int(input("Player4, choose a option using a number: "))
                        else:
                            selection_player4 = 0

                    #esta la parte del desafio
                    situation_player1_challenge =""
                    situation_player1_counterattack =""
                    if number_players ==3:
                        #esta es la parte del desafio para 3 jugadores en el turno del jugador1
                        #si algun player (no el de turno) elige 1(challenge)
                        #y player1 elige algo que se puede desafiar
                        if (selection_player2 == 1 or selection_player3 == 1) and (selection_player1==4 or selection_player1 ==5
                            or selection_player1 ==6 or selection_player1==7):

                            print()
                            #si los dos desafían:
                            if selection_player2 ==1 and selection_player3 ==1:
                                print("Whoever challenges player1, will be chosen at random.")
                                random_1 = random.randint(2,3)
                            #si no desafían ambos:
                            elif selection_player2 ==1 and selection_player3 !=1:
                                random_1 =2
                            elif selection_player2 !=1 and selection_player3 ==1:
                                random_1 = 3
                            list_situation_player1_challenge =[]
                            challenge_player1(number_players,random_1,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player1, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player1_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player1_challenge =list_situation_player1_challenge[0]
                            list_situation_player1_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                        #aqui comienza el contraatque para el jugador1
                        if (selection_player2 ==2 or selection_player3 ==2) and (selection_player1 ==2 or selection_player1 ==5 or 
                                selection_player1 ==6) and situation_player1_challenge != "lose":
                                
                                if selection_player2 ==2 and selection_player3 !=2:
                                    random_1 =2
                                if selection_player2 !=2 and selection_player3 ==2:
                                    random_1 =3
                                if selection_player2 ==2 and selection_player3 ==2:
                                    print("Whoever counterattacks player1, will be chosen at random")
                                    random_1 =random.randint(2,3)

                                list_situation_player1_counterattack = []
                                counterattack_player1(random_1,selection_player1,list_situation_player1_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)

                                situation_player1_counterattack = list_situation_player1_counterattack[0]
                                list_situation_player1_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    if number_players == 4:
                        #esta es la parte del desafio para 4 jugadores en el turno del jugador1
                        if (selection_player2 == 1 or selection_player3 == 1 or selection_player4==1) and (selection_player1==4 or selection_player1 ==5
                            or selection_player1 ==6 or selection_player1==7):
                            
                            if selection_player2 ==1 and selection_player3 !=1 and selection_player4 !=1:
                                random_1 = 2
                            elif selection_player2 !=1 and selection_player3 ==1 and selection_player4 !=1:
                                random_1 =3
                            elif selection_player2 !=1 and selection_player3 !=1 and selection_player4 ==1:
                                random_1 =4
                            elif selection_player2 ==1 and selection_player3 ==1 and selection_player4 !=1:
                                print("Whoever challenges player1, will be chosen at random")
                                random_1 = random.randint(2,3)
                            elif selection_player2 ==1 and selection_player3 !=1 and selection_player4 ==1:
                                print("Whoever challenges player1, will be chosen at random")
                                random_1 = random.randint(2,3)
                                if random_1 ==3:
                                    random_1 =4
                            elif selection_player2 !=1 and selection_player3 ==1 and selection_player4 ==1:
                                print("Whoever challenges player1, will be chosen at random")
                                random_1 = random.randint(3,4)
                            elif selection_player2 ==1 and selection_player3 ==1 and selection_player4 ==1:
                                print("Whoever challenges player1, will be chosen at random")
                                random_1 =random.randint(2,4)
                            list_situation_player1_challenge =[]
                            challenge_player1(number_players,random_1,list_cards_player1,list_cards_player2,
                                                list_cards_player3, list_cards_player4, selection_player1, list_rest_of_deck,
                                                list_eliminated_cards_player1,list_eliminated_cards_player2, 
                                                list_eliminated_cards_player3, list_eliminated_cards_player4, list_situation_player1_challenge)
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                            situation_player1_challenge = list_situation_player1_challenge[0]
                            list_situation_player1_challenge =[]
                            life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)


                        #esta es la parte del contraattaque para 4 jugadores en el turno del player1
                        if (selection_player2 ==2 or selection_player3 ==2 or selection_player4 ==2 ) and (selection_player1 ==2 or 
                            selection_player1 ==5 or selection_player1 ==6) and situation_player1_challenge != "lose":
                                print("Counterattack!")
                                if selection_player2 ==2 and selection_player3 !=2 and selection_player4 !=2:
                                    random_1 =2
                                if selection_player2 !=2 and selection_player3 ==2 and selection_player4 !=2:
                                    random_1 =3
                                if selection_player2 !=2 and selection_player3 !=2 and selection_player4 ==2:
                                    random_1 =4
                                if selection_player2 ==2 and selection_player3 ==2 and selection_player4 !=2:
                                    print("Whoever counterattacks player1, will be chosen at random")
                                    random_1 =random.randint(2,3)
                                if selection_player2 ==2 and selection_player3 !=2 and selection_player4 ==2:
                                    print("Whoever counterattacks player1, will be chosen at random")
                                    random_1 =random.randint(2,3)
                                    if random_1 ==3:
                                        random_1 = 4
                                if selection_player2 !=2 and selection_player3 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player1, will be chosen at random")
                                    random_1 =random.randint(3,4)

                                if selection_player2 ==2 and selection_player3 ==2 and selection_player4 ==2:
                                    print("Whoever counterattacks player1, will be chosen at random")
                                    random_1 =random.randint(2,4)

                                list_situation_player1_counterattack = []
                                counterattack_player1(random_1,selection_player1,list_situation_player1_counterattack,list_cards_player1,
                                                    list_cards_player2, list_cards_player3,list_cards_player4,number_players,
                                                    list_eliminated_cards_player1,list_eliminated_cards_player2,list_eliminated_cards_player3,
                                                    list_eliminated_cards_player4,list_players)
                                                    
                                situation_player1_counterattack = list_situation_player1_counterattack[0]
                                list_situation_player1_counterattack = []
                                life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)

                    #aca se ven las acciones del player1 despues de los desafios o contra_ataques, hay que revisarlo
                    
                    if situation_player1_challenge == "win" and situation_player1_counterattack =="win":
                        player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player1_challenge =="win" and situation_player1_counterattack =="":
                        player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player1_challenge =="" and situation_player1_counterattack =="win":
                        player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    if situation_player1_challenge =="" and situation_player1_counterattack =="":
                        player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)
                    life_players(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
                    
                    if selection_player1 ==5 and situation_player1_challenge =="lose":
                        list_players[0].coins_game +=3

            elif list_players[0].coins_game >= 10:
                selection_player1 = 3
                list_players[0].coins_game -=7
                player1_actions(selection_player1,list_players, list_cards_player1,list_cards_player2,list_cards_player3,
                                list_cards_player4,list_rest_of_deck, list_eliminated_cards_player1, list_eliminated_cards_player2,
                                list_eliminated_cards_player3, list_eliminated_cards_player4)

        #aqui inicia el turno del player2
        if list_players[1].live_game =="yes":
            print("Player2, it's your turn:")
            game_player2(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            print("Player2 is no longer in the game.")
        #aqui inicia el turno del player3
        if list_players[2].live_game =="yes":
            print("Player3, it's your turn:")
            game_player3(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
        else:
            print("Player3 is no longer in the game.")
        if number_players==4:
        #aqui inicia el turno del player4
            
            if list_players[3].live_game =="yes":
                print("Player4, it's your turn:")
                game_player4(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards,list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
            else:
                print("Player4 is no longer in the game.")
        else: 
            sys.exit("Player1 has won the game!")
            


    


def three_players(deck,number_players):
    player1 = Person("Player1",int(2),"yes")
    player2 = Person("Player2",int(2),"yes")
    player3 = Person("Player3",int(2),"yes")

    list_players = [player1,player2,player3]
    """
    if number_players ==4:
        player4 = Person("Player4",int(2),"yes")
        list_players.append(player4)
    """

    list_cards_player1 = []
    list_cards_player2 = []
    list_cards_player3 = []
    list_cards_player4 = []
    list_rest_of_deck = []
    players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_rest_of_deck,number_players)
    #en player_cards se otorgan las cartas a cada jugador y las cartas del mazo

    card1 = Card(list_cards_player1[0])
    card2 = Card(list_cards_player1[1])
    card3 = Card(list_cards_player2[0])
    card4 = Card(list_cards_player2[1])
    card5 = Card(list_cards_player3[0])
    card6 = Card(list_cards_player3[1])
    card7 = Card(list_rest_of_deck[0])
    card8 = Card(list_rest_of_deck[1])
    card9 = Card(list_rest_of_deck[2])
    card10 = Card(list_rest_of_deck[3])
    card11 = Card(list_rest_of_deck[4])
    card12 = Card(list_rest_of_deck[5])
    card13 = Card(list_rest_of_deck[6])
    card14 = Card(list_rest_of_deck[7])
    card15 = Card(list_rest_of_deck[8])
    list_all_cards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15]
    #distribution of cards haca un print de como los jugadores estan colocados y
    #printea las cartas de cada jugador
    distribution_of_cards(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
    
    list_eliminated_cards_player1 = []
    list_eliminated_cards_player2 = []
    list_eliminated_cards_player3 = []
    list_eliminated_cards_player4 = []
    #en game se  inicia los turnos de los jugadores con sus respectivas acciones
    game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards, list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)






def four_players(deck,number_players):
    player1 = Person("Player1",int(2),"yes")
    player2 = Person("Player2",int(2),"yes")
    player3 = Person("Player3",int(2),"yes")
    player4 = Person("Player4",int(2),"yes")
    list_players = [player1,player2,player3,player4]

    list_cards_player1 = []
    list_cards_player2 = []
    list_cards_player3 = []
    list_cards_player4 = []
    list_rest_of_deck = []
    players_cards(deck,list_cards_player1,list_cards_player2, list_cards_player3,list_cards_player4,list_rest_of_deck,number_players)
    #en player_cards se otorgan las cartas a cada jugador y las cartas del mazo

    card1 = Card(list_cards_player1[0])
    card2 = Card(list_cards_player1[1])
    card3 = Card(list_cards_player2[0])
    card4 = Card(list_cards_player2[1])
    card5 = Card(list_cards_player3[0])
    card6 = Card(list_cards_player3[1])
    card7 = Card(list_cards_player4[0])
    card8 = Card(list_cards_player4[1])
    card9 = Card(list_rest_of_deck[0])
    card10 = Card(list_rest_of_deck[1])
    card11 = Card(list_rest_of_deck[2])
    card12 = Card(list_rest_of_deck[3])
    card13 = Card(list_rest_of_deck[4])
    card14 = Card(list_rest_of_deck[5])
    card15 = Card(list_rest_of_deck[6])
    list_all_cards = [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,card13,card14,card15]
    #distribution of cards haca un print de como los jugadores estan colocados y
    #printea las cartas de cada jugador
    distribution_of_cards(list_players,list_cards_player1,list_cards_player2,list_cards_player3,list_cards_player4,number_players)
    
    list_eliminated_cards_player1 = []
    list_eliminated_cards_player2 = []
    list_eliminated_cards_player3 = []
    list_eliminated_cards_player4 = []
    #en game se inicia los turnos de los jugadores con sus respectivas acciones
    game(list_players,number_players,list_cards_player1,list_cards_player2,list_cards_player3,
        list_cards_player4,list_rest_of_deck,list_all_cards, list_eliminated_cards_player1,
        list_eliminated_cards_player2, list_eliminated_cards_player3, list_eliminated_cards_player4)
    

    


def main():
    #esta parte es para crear el mazo de cartas y luego revolverlas
    deck = Card("Deck")
    deck.deck_cards()
    deck.deck_random_cards()

    while True:
        number_players = int(input("How many players will play this game? Type 3 or 4, using a number : "))
        print("The cards can only be seen by the player of the turn")
        if number_players == 3:
            three_players(deck,number_players)
            break
        if number_players ==4:
            four_players(deck,number_players)
            break
        else:
            print("The number you typed is not valid, please try again.")
    

    


if __name__ == "__main__":
    main()

