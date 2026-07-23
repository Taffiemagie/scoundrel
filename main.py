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
#Weapon is a list: the card at index 0 will be the weapon, the rest will be monsters.
weapon = ["None"]

#Sets the variables for a new game then shuffles the deck and creates the room
def new_game():
    global room
    global hp
    global scoundrel_deck
    global weapon
    room = []
    hp = 20
    weapon = ["None"]
    scoundrel_deck.new()
    #Marks the list index for removal, then removes it from the for loop. Removing during the for loop causes an out of bounds error.
    tmp_toremove = []
    for card in scoundrel_deck.card_list:
        if card.value == 1:
            tmp_toremove.append(card)
        elif card.value >=11 and (card.suit == "Diamonds" or card.suit == "Hearts"):
            tmp_toremove.append(card)
    for card in tmp_toremove:
        scoundrel_deck.card_list.remove(card)
    scoundrel_deck.shuffle_deck()
    for i in range(4):
        room.append(scoundrel_deck.draw())

#Shows the appropriate menu according to cards in the room
def show_menu():
    global room
    global hp
    global scoundrel_deck
    global weapon
    if len(weapon) == 1:
        print(f"~ HP:{hp} Cards left:{len(scoundrel_deck.card_list)} ~\n~ Weapon:{weapon[0]} ~\n~ Select a card from below or press \'help\' ~")
    elif len(weapon) > 1:
        print(f"~ HP:{hp} Cards left:{len(scoundrel_deck.card_list)} ~\n~ Weapon:{weapon[0]} Slain monster:{weapon[-1]} ~\n~ Select a card from below or press \'help\' ~")
    card_num = 1
    for card in room:
        print(f"{card_num}: {card.uname}")
        card_num += 1

#Allows the user to select a option and updates global variables
def play_card():
    global room

#Gameplay loop.
def __main__():
    new_game()
    show_menu()

__main__()