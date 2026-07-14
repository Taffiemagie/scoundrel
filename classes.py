#!/bin/python3

import random

#Class representing one playing card
class card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        self.uname = f"{self.value} of {self.suit}"

#Class representing a deck of 52 standard playing cards
class deck_52:
    def __init__(self):
        self.max_cards = 52
        self.card_list = []
        self.suits = ["Spades","Clubs","Hearts","Diamonds"]
        self.values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    
    #Goes through the list of suits and values to add all the cards to the deck
    def new(self):
        for suit in self.suits:
            for value in self.values:
                self.card_list.append(card(suit,value))
    
    #Iterates through the card list and prints them.
    def list(self):
        for card in self.card_list:
            print(card.uname)

    #Shuffles deck
    def shuffle_deck(self):
        random.shuffle(self.card_list)

    #Pulls top card from deck
    def draw(self):
        return self.card_list.pop(0)