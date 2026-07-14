#!/bin/python3

"""
Program Name: Scoundrel
Program Purpose: Play Scoundrel
Author: cake_eater
"""

import classes

#Intro menu and gameplay loop.
def __main__():
    scoundrel_deck = classes.deck_52()
    scoundrel_deck.new()
    scoundrel_deck.list()
    scoundrel_deck.shuffle_deck()
    print("----------")
    scoundrel_deck.list()

__main__()