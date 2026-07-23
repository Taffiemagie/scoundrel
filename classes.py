#!/bin/python3

import random

#Class representing one playing card
class card:
    face_cards = {0:"Joker", 1:"Ace", 11:"Jack", 12:"Queen", 13:"King"}
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
        #Below refers to the above dictionary and changes the user friendly name to the face card
        if self.value in self.face_cards:
            self.uname = f"{card.face_cards[self.value]} of {self.suit}"
        else:
            self.uname = f"{self.value} of {self.suit}"

#Class representing a deck of 52 standard playing cards (No Jokers)
class deck_52:
    suits = ["Spades","Clubs","Hearts","Diamonds"]
    values = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    def __init__(self):
        self.max_cards = 52
        self.card_list = []
    
    #Goes through the list of suits and values to add all the cards to the deck
    def new(self):
        self.card_list = []
        for suit in deck_52.suits:
            for value in deck_52.values:
                self.card_list.append(card(suit,value))
    
    #Iterates through the card list and prints them.
    def list(self):
        for card in self.card_list:
            print(card.uname)

    #Shuffles deck
    def shuffle_deck(self):
        random.shuffle(self.card_list)

    #Pulls top card from deck (Last card in the list)
    def draw(self):
        return self.card_list.pop()