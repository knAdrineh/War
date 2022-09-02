'''
The game is called war
there is a deck of 52 cards
first we split them evenly between two player
then each player take out a card , who ever has the larger value gets to keep both cards
in case there is a tie each palyer take out 3 cards without watching and another card
who ever has the bigger value gets to keep the 10 cards
'''
from card import Card
from card import Deck
from card import Player

def print_deck(ls):
    count = 0
    for cards in new_deck.all_cards:
        if count % 4 == 0:
            print(cards)
        else:
            print(cards, " ", end="")
        count += 1

    print()
    print()

#creating a new deck
new_deck = Deck()
new_deck.shuffle()



#player 1
player1 = Player("Becky")
player1.add_card(new_deck.all_cards[:26])


#player 2
player2 = Player("John")
player2.add_card(new_deck.all_cards[26:])


game_on = True
rnd = 0
while game_on:
    rnd +=1
    print(f"Round {rnd}")
    print(f"{player1}")
    print(f"{player2}")
    cards_ls = []
    #has any of the players
    game_on = len(player1.all_cards) != 0 and len(player2.all_cards) != 0
    #player 1 takes out a card
    card1 = player1.remove_one()
    #player 2 take out a card
    card2 = player2.remove_one()


    cards_ls.append(card1)
    cards_ls.append(card2)
    at_war = True
    while at_war and game_on :
        if card1.value > card2.value:
            print(f"{player1.name} beats {player2.name} : {card1} | {card2} ")
            player1.add_card(cards_ls)
            cards_ls.clear()
            at_war = False

        elif card1.value < card2.value:
            print(f"{player2.name} beats {player1.name} : {card2} | {card1} ")
            player1.add_card(cards_ls)
            cards_ls.clear()
            cards_ls.clear()
            at_war = False
        else:
            print(f"It's a Tie!\n {player2.name} , {player1.name} : {card1} | {card2} ")
            if len(player1.all_cards) < 5 :
                player1.all_cards.clear()
                game_on = False
                at_war = False
            elif len(player2.all_cards) < 5:
                player1.all_cards.clear()
                game_on = False
                at_war = False
            else:
                #player 1 takes out 3 cards
                cards_ls.append(player1.remove_one())
                cards_ls.append(player1.remove_one())
                cards_ls.append(player1.remove_one())
                card1 = player1.remove_one()
                #player 2 takes out 3 cards
                cards_ls.append(player2.remove_one())
                cards_ls.append(player2.remove_one())
                cards_ls.append(player2.remove_one())
                at_war = True

if len(player1.all_cards) == 0:
    print(f"Congrats {player2.name} won the game. {player2}")
else:
    print(f"Congrats {player1.name} won the game. {player1}")