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
    COLOUR_RESET = "\033[0m"
    COLOUR_RED = "\033[31m"
    COLOUR_BLACK = "\033[30m"
    #Only shows last slain monster if a monster has been slain
    if weapon[0] == "None":
        print(f"\n~ HP:{hp} Cards left:{len(scoundrel_deck.card_list) + len(room)} ~\n~ Weapon:{weapon[0]} ~\n~ Select a card from below or enter \'help\' ~")
    elif weapon[-1].suit == "Diamonds":
        print(f"\n~ HP:{hp} Cards left:{len(scoundrel_deck.card_list) + len(room)} ~\n~ Weapon:{COLOUR_RED}{weapon[0].uname}{COLOUR_RESET} ~\n~ Select a card from below or enter \'help\' ~")
    elif len(weapon) >= 2:
        print(f"\n~ HP:{hp} Cards left:{len(scoundrel_deck.card_list) + len(room)} ~\n~ Weapon:{COLOUR_RED}{weapon[0].uname}{COLOUR_RESET)} ~ Last Slain Monster:{COLOUR_BLACK}{weapon[-1].uname}{COLOUR_RESET} ~\n~ Select a card from below or enter \'help\' ~")
    card_num = 1
    for card in room:
        if card.suit == "Diamonds" or card.suit == "Hearts":
            print(f"{card_num}: {COLOUR_RED}{card.uname}{COLOUR_RESET}")
        elif card.suit == "Clubs" or card.suit == "Spades":
            print(f"{card_num}: {COLOUR_BLACK}{card.uname}{COLOUR_RESET}")
        card_num += 1

#Allows the user to play a card
def play():
    global room
    global hp
    global scoundrel_deck
    global weapon
    choice = input("~ ").lower()
    valid_inputs = ['1','2','3','4','help','h']
    while choice not in valid_inputs:
        choice = input("~ Invalid input ~\n~ ").lower()
    if choice in valid_inputs[:4]:
        choice_card = room[int(choice)-1]
        #Performs actions according to the card's suit and conditions
        match choice_card.suit:
            case "Hearts":
                if hp + choice_card.value < 20:
                    hp += choice_card.value
                else:
                    hp = 20
                room.remove(choice_card)
            case "Diamonds":
                weapon = [room.pop(int(choice)-1)]
            #Logically assigns damage base on weapon and slain enemies
            case "Clubs" | "Spades":
                #Case where there is no weapon
                if weapon[-1] == "None":
                    hp -= choice_card.value
                    room.remove(choice_card)
                #Case where the weapon has not slain any monsters
                elif weapon[-1].suit == "Diamonds":
                    slay = input(f"~ Slay the {choice_card.uname} with {weapon[0].uname} [w] or hands? [h] ~ ")
                    while slay.lower() != 'w' and slay.lower() != 'h':
                        slay = input(f"~ Incorrect input ~\n~ Slay the {choice_card.uname} with {weapon[0].uname} [w] or hands? [h] ~ ")
                    if slay.lower() == 'w':
                        if choice_card.value > weapon[0].value:
                            hp -= (choice_card.value - weapon[-1].value)
                        weapon.append(choice_card)
                    elif slay.lower() == 'h':
                        hp -= choice_card.value
                    room.remove(choice_card)
                #Case where the weapon has slain monster(s)
                elif weapon[-1].suit == "Spades" or weapon[-1].suit == "Clubs":
                    #Checks if monster is lower value than previously slain monster
                    if choice_card.value < weapon[-1].value:
                        slay = input(f"~ Slay the {choice_card.uname} with {weapon[0].uname} [w] or hands? [h] ~")
                        while slay.lower() != 'w' and slay.lower() != 'h':
                            slay = input(f"~ Incorrect input ~\n~ Slay the {choice_card.uname} with {weapon[0].uname} [w] or hands? [h] ~ ")
                        if slay == 'w':
                            if choice_card.value > weapon[0].value:
                                hp -= choice_card.value - weapon[0].value
                            weapon.append(choice_card)
                        elif slay == 'h':
                            hp -= choice_card.value
                    elif choice_card.value > weapon[-1].value:
                        hp -= choice_card.value
                    room.remove(choice_card)
    

#Gameplay loop.
def __main__():
    global room
    global hp
    global scoundrel_deck
    global weapon
    new_game()
    while hp > 0 and (len(scoundrel_deck.card_list) + len(room) > 0):
        show_menu()
        play()
        if len(room) == 1 and len(scoundrel_deck.card_list) > 0:
            for i in range(3):
                room.append(scoundrel_deck.draw())
    if hp <= 0:
        print("GG you died shake my hand")
    elif hp > 0:
        print("Nice one bro you lived")

__main__()