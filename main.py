#!/bin/python3

"""
Program Name: Scoundrel
Program Purpose: Play Scoundrel
Author: cake_eater
"""

import classes
room = []
hp = 0
scoundrel_deck = classes.deck_52()

#Sets the variables for a new game then shuffles the deck and creates the room
def new_game(deck):
    global room
    global hp
    global scoundrel_deck
    hp = 10
    scoundrel_deck.new()
    scoundrel_deck.shuffle_deck()
    for i in range(4):
        room.append(deck.draw())

#Shows the appropriate menu according to cards in the room
def show_menu():
    global room
    print("~ Select a card from below or press \'help\' ~")
    card_num = 1
    for card in room:
        print(f"{card_num}: {card.uname}")
        card_num += 1

#Gameplay loop.
def __main__():
    new_game(scoundrel_deck)
    show_menu()

__main__()