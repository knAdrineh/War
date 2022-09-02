'''
Card class
should know the suit, rank, value of the card
'''
import random
suits = ('♥', '♦', '♠', '♣')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

'''
builds each card
'''
class Card():

    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank.capitalize()
        self.value = values[rank]

    def __str__(self):
        '''
        1 of Ace

        :return:
        '''
        return self.rank + " of " + self.suit

'''
the deck is the random order of cards

'''
class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                '''
                create the deck of cards
                '''
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def del_one(self):
        return self.all_cards.pop()

'''
each player holds on the cards
'''
class Player():

    def __init__(self, name):
        self.name = name
        self.all_cards =[]

    def remove_one(self):
        if len(self.all_cards) != 0:
            return self.all_cards.pop(0)

    def add_card(self,new):
        if type(new) == type([]):
            #list of multiple card objects
            self.all_cards.extend(new)
        else:
            #one card object
            self.all_cards.append(new)

    def __str__(self):
        return f'player {self.name} has {len(self.all_cards)} cards.'

