#! /usr/bin/env python3
# coding: UTF-8

""" Labyrinth game in which mac gyver must retrieve all objects
to kill the guardian and escape """

import os

# import the pygame library and this module
import pygame
from pygame.locals import *
# initialize the pygame library
pygame.init()

from classes import *

def labyrinth_game():
    """For replay the game"""
    # indicates the way to find the images to be used for the program
    os.chdir("C:/Users/Carole/program_python/Program/Labyrinth/ressources")

    Labyrinth().blit_pictures()
    Objects().color_blit_objects()
    Person().color_blit_person()

    pygame.display.flip()


    # infinite loop
    play = 1
    while play:

        for event in pygame.event.get(): 
            # if press the right arrow key? mac gyver goes right
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_RIGHT:
                new_person = Person()
                new_person.movement_right()    
            # if press the left arrow key, mac gyver goes left
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_LEFT:
                new_person = Person()
                new_person.movement_left() 
            # if press the up arrow key, mac gyver goes up
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_UP:
                new_person = Person()
                new_person.movement_up() 
            # if press the down arrow key, mac gyver goes down
            # adding the last position of mac gyver in the list PATH_TRAVELED_MAC_GYVER
            if event.type == KEYDOWN and event.key == K_DOWN:
                new_person = Person()
                new_person.movement_down()
            """# if mac gyver goes down on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_DOWN \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, - 40)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur - 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur - 40
                    init_event()
            # if mac gyver goes up on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_UP \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(0, 40)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur + 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur + 40
                    init_event()
            # if mac gyver goes right on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_RIGHT \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    moving_mac_gyver = moving_mac_gyver.move(- 40, 0)
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle - 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle - 40] = valeur
                    init_event()
            # if mac gyver goes left on the coordinates of a wall
            # mac gyver returns to its original position
            if event.type == KEYDOWN and event.key == K_LEFT \
                and path_position_list.count(last_location_mac_gyver_tuple) == 0:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    del path_traveled_mac_gyver[-1]
                    moving_mac_gyver = moving_mac_gyver.move(40, 0)
                    last_location_mac_gyver_tuple = (cle + 40, valeur)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle + 40] = valeur
                    init_event()
            # if the player arrives on the guardien, he can no longer move
            if last_location_mac_gyver_dict == {440: - 40}:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    last_location_mac_gyver_tuple = (cle, valeur + 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur + 40
                    init_event()
            if path_traveled_mac_gyver.count((440, 0)) == 1 \
                and last_location_mac_gyver_dict == {440: 40}:
                for cle, valeur in last_location_mac_gyver_dict.items():
                    del path_traveled_mac_gyver[-1]
                    last_location_mac_gyver_tuple = (cle, valeur - 40)
                    last_location_mac_gyver_dict.clear()
                    last_location_mac_gyver_dict[cle] = valeur - 40
                    init_event()
            # if mac gyver is passed on the neddle
            # +1 to the counter of objects and the needle disappears from the window
            if path_traveled_mac_gyver.count(needle_position) == 1:
                counter_objects = counter_objects + 1
                needle_position = WINDOW.blit(needle_picture, (600, 600))
            # if mac gyver is passed on the ether
            # +1 to the counter of objects and the ether disappears from the window
            if path_traveled_mac_gyver.count(ether_position) == 1:
                counter_objects = counter_objects + 1
                ether_position = WINDOW.blit(ether_picture, (600, 600))
            # if mac gyver is passed on the plastic_tube
            # +1 to the counter of objects and the syringe disappears from the window
            if path_traveled_mac_gyver.count(plastic_tube_position) == 1:
                counter_objects = counter_objects + 1
                plastic_tube_position = WINDOW.blit(plastic_tube_picture, (600, 600))
            # if mac gyver have not the 3 objects and arrives at the guardian
            # the messages "perdu !", "rejouer" and "quitter" is displayed
            # if the player clicks on "rejouer", the program restarts,
            # on "quitter", the program stops
            if last_location_mac_gyver_dict == {440: 0} and counter_objects != 3:
                background()
                WINDOW.blit(guardian_picture, (440, 0))
                WINDOW.blit(grave_picture, (200, 200))
                WINDOW.blit(replay_picture, (0, 520))
                WINDOW.blit(quit_picture, (520, 520))
                pygame.display.flip()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                    and event.pos[0] > 520 and event.pos[1] > 520:
                    pygame.quit()
                    quit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1 \
                    and event.pos[0] < 80 and event.pos[1] > 520:
                    labyrinth_game()
            # if mac gyver have the 3 objects and arrives at the guardian
            # the message "gagné !" is displayed and the program quits
            if last_location_mac_gyver_dict == {440: 0} and counter_objects == 3:
                background()
                WINDOW.blit(won_picture, (120, 120))
                pygame.display.flip()
                pygame.quit()
                quit()"""
labyrinth_game()
