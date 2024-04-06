# main.py

from Classes.deck import Deck
from Classes.player import Player

playing = True

import random
suits = {'Hearts', "Diamonds", "Spades", "Clubs"}
ranks = {"Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 'Jack', 'Queen', "King", "Ace"}
values = {"Two":2,"Three":3,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":11,
        "Queen":12, "King":13, 'Ace':14}

#game setup
player_one = Player('One')
player_two = Player('Two')

new_deck = Deck(values)
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

game_on = True
round_num = 0

round_num = 0
while game_on:

    round_num += 1
    print(f'Round {round_num}')
        
    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two Wins!')
        game_on = False
        break
            
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One Wins!')
        game_on = False
        break
    #start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
        
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    #while at_war
    at_war = True
    
    while at_war:
        
    
        if player_one_cards[-1].value > player_two_cards[-1].value:
            
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            at_war = False
            
    
        elif player_one_cards[-1].value < player_two_cards[-1].value:
            
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            
            at_war = False
        
        else:
            print("WAR!")
            
            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war')
                print('PLAYER TWO WINS!')
                game_on = False
                break
                
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war')
                print('PLAYER ONE WINS!')
                game_on = False
                break
                
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())