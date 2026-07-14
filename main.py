#!/bin/python3

"""
Program Name: Scoundrel
Program Purpose: Play Scoundrel
Author: cake_eater
"""

import classes

#Creates and plays through a new game
def new_game(deck):
    playerhp = 10
    room = []
    for i in range(4):
        room.append(deck.draw())
    for card in room:
        print(card.uname)

#Intro menu and gameplay loop.
def __main__():
    scoundrel_deck = classes.deck_52()
    scoundrel_deck.new()
    scoundrel_deck.shuffle_deck()
    new_game(scoundrel_deck)

__main__()