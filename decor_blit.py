#! /usr/bin/env python3
# coding: utf-8

import os
import pygame
from labyrinth_position import *
from pygame.locals import *

pygame.init() 


os.chdir("C:/Users/Carole/program_python/program/labyrinth/ressource")
"""chemin dans lequel se trouve les images utilisées dans ce script"""
window = pygame.display.set_mode((600, 600)) 
"""Affichage de la fenêtre en taille 600/600 pixels"""

def background():
    """Script qui permet de réunir plusieurs images (dans l'esprit puzzle) 
    afin de créer un fond d'écran et qui permet de l'afficher dans une fenêtre"""
    
    ground_picture = pygame.image.load("ground.png").convert_alpha()
    wall_top_left_picture = pygame.image.load("top_left.png").convert_alpha()
    wall_top_right_picture = pygame.image.load("top_right.png").convert_alpha()
    wall_low_right_picture = pygame.image.load("low_right.png").convert_alpha()
    wall_low_left_picture = pygame.image.load("low_left.png").convert_alpha()
    wall_horizontal_picture = pygame.image.load("horizontal.png").convert_alpha()
    wall_vertical_picture = pygame.image.load("vertical.png").convert_alpha()
    """récupèration des images de mon fond d'écran"""
    
    

    """Fonction qui permet de traduire les listes ci-dessus 
    afin de coller les images et créer le fond d'écran désiré"""
    def wall_ground_location(line_number, index, number_picture, picture): # on indique des paramètres afin d'utiliser une seule fonction 
        line_finale=[]  # on crée une liste vide                      pour fabriquer l'ensemble du fond d'écran
        i=0             # i : notre compteur
        for i, elt in enumerate(line_number):     # va permettre de parcourir tous les élèments de la ligne définie dans les paramètres 
            if elt == number_picture:                   # si un des élèments correspond au number_picture demandé,
                line_finale.append(((i*40), index))     # les coordonnées de son emplacement s'ajoute à ma liste vide
        i+=1                                            # permet de prendre en compte les élèments de ma liste 1 à 1 jusqu'à sa fin
        for location in line_finale:
            window.blit(picture, (location))            # parcours les valeurs de ma nouvelle liste afin de traduire les coordonnées
                                                        # et coller les images à la bonne place pour former le fond d'écran
                                                        
    wall_ground_location(line_0, 0, "0", wall_top_left_picture)    
    wall_ground_location(line_1, 40, "0", wall_top_left_picture)       # appel de la fonction wall_location à de multiples reprises avec différents paramètres
    wall_ground_location(line_2, 80, "0", wall_top_left_picture)       # afin de prendre en compte toutes les lignes et toutes les images
    wall_ground_location(line_3, 120, "0", wall_top_left_picture)
    wall_ground_location(line_4, 160, "0", wall_top_left_picture)
    wall_ground_location(line_5, 200, "0", wall_top_left_picture)
    wall_ground_location(line_6, 240, "0", wall_top_left_picture)
    wall_ground_location(line_7, 280, "0", wall_top_left_picture)
    wall_ground_location(line_8, 320, "0", wall_top_left_picture)
    wall_ground_location(line_9, 360, "0", wall_top_left_picture)
    wall_ground_location(line_10, 400, "0", wall_top_left_picture)
    wall_ground_location(line_11, 440, "0", wall_top_left_picture)
    wall_ground_location(line_12, 480, "0", wall_top_left_picture)
    wall_ground_location(line_13, 520, "0", wall_top_left_picture)
    wall_ground_location(line_14, 560, "0", wall_top_left_picture)

    wall_ground_location(line_0, 0, "1", wall_top_right_picture)
    wall_ground_location(line_1, 40, "1", wall_top_right_picture)
    wall_ground_location(line_2, 80, "1", wall_top_right_picture)
    wall_ground_location(line_3, 120, "1", wall_top_right_picture)
    wall_ground_location(line_4, 160, "1", wall_top_right_picture)
    wall_ground_location(line_5, 200, "1", wall_top_right_picture)
    wall_ground_location(line_6, 240, "1", wall_top_right_picture)
    wall_ground_location(line_7, 280, "1", wall_top_right_picture)
    wall_ground_location(line_8, 320, "1", wall_top_right_picture)
    wall_ground_location(line_9, 360, "1", wall_top_right_picture)
    wall_ground_location(line_10, 400, "1", wall_top_right_picture)
    wall_ground_location(line_11, 440, "1", wall_top_right_picture)
    wall_ground_location(line_12, 480, "1", wall_top_right_picture)
    wall_ground_location(line_13, 520, "1", wall_top_right_picture)
    wall_ground_location(line_14, 560, "1", wall_top_right_picture)

    wall_ground_location(line_0, 0, "2", wall_low_right_picture)
    wall_ground_location(line_1, 40, "2", wall_low_right_picture)
    wall_ground_location(line_2, 80, "2", wall_low_right_picture)
    wall_ground_location(line_3, 120, "2", wall_low_right_picture)
    wall_ground_location(line_4, 160, "2", wall_low_right_picture)
    wall_ground_location(line_5, 200, "2", wall_low_right_picture)
    wall_ground_location(line_7, 280, "2", wall_low_right_picture)
    wall_ground_location(line_8, 320, "2", wall_low_right_picture)
    wall_ground_location(line_9, 360, "2", wall_low_right_picture)
    wall_ground_location(line_10, 400, "2", wall_low_right_picture)
    wall_ground_location(line_11, 440, "2", wall_low_right_picture)
    wall_ground_location(line_12, 480, "2", wall_low_right_picture)
    wall_ground_location(line_13, 520, "2", wall_low_right_picture)
    wall_ground_location(line_14, 560, "2", wall_low_right_picture)

    wall_ground_location(line_0, 0, "3", wall_low_left_picture)
    wall_ground_location(line_1, 40, "3", wall_low_left_picture)
    wall_ground_location(line_2, 80, "3", wall_low_left_picture)
    wall_ground_location(line_3, 120, "3", wall_low_left_picture)
    wall_ground_location(line_4, 160, "3", wall_low_left_picture)
    wall_ground_location(line_5, 200, "3", wall_low_left_picture)
    wall_ground_location(line_6, 240, "3", wall_low_left_picture)
    wall_ground_location(line_7, 280, "3", wall_low_left_picture)
    wall_ground_location(line_8, 320, "3", wall_low_left_picture)
    wall_ground_location(line_9, 360, "3", wall_low_left_picture)
    wall_ground_location(line_10, 400, "3", wall_low_left_picture)
    wall_ground_location(line_11, 440, "3", wall_low_left_picture)
    wall_ground_location(line_12, 480, "3", wall_low_left_picture)
    wall_ground_location(line_13, 520, "3", wall_low_left_picture)
    wall_ground_location(line_14, 560, "3", wall_low_left_picture)

    wall_ground_location(line_0, 0, "4", wall_horizontal_picture)
    wall_ground_location(line_1, 40, "4", wall_horizontal_picture)
    wall_ground_location(line_2, 80, "4", wall_horizontal_picture)
    wall_ground_location(line_3, 120, "4", wall_horizontal_picture)
    wall_ground_location(line_4, 160, "4", wall_horizontal_picture)
    wall_ground_location(line_5, 200, "4", wall_horizontal_picture)
    wall_ground_location(line_6, 240, "4", wall_horizontal_picture)
    wall_ground_location(line_7, 280, "4", wall_horizontal_picture)
    wall_ground_location(line_8, 320, "4", wall_horizontal_picture)
    wall_ground_location(line_9, 360, "4", wall_horizontal_picture)
    wall_ground_location(line_10, 400, "4", wall_horizontal_picture)
    wall_ground_location(line_11, 440, "4", wall_horizontal_picture)
    wall_ground_location(line_12, 480, "4", wall_horizontal_picture)
    wall_ground_location(line_13, 520, "4", wall_horizontal_picture)
    wall_ground_location(line_14, 560, "4", wall_horizontal_picture)

    wall_ground_location(line_0, 0, "5", wall_vertical_picture)
    wall_ground_location(line_1, 40, "5", wall_vertical_picture)
    wall_ground_location(line_2, 80, "5", wall_vertical_picture)
    wall_ground_location(line_3, 120, "5", wall_vertical_picture)
    wall_ground_location(line_4, 160, "5", wall_vertical_picture)
    wall_ground_location(line_5, 200, "5", wall_vertical_picture)
    wall_ground_location(line_6, 240, "5", wall_vertical_picture)
    wall_ground_location(line_7, 280, "5", wall_vertical_picture)
    wall_ground_location(line_8, 320, "5", wall_vertical_picture)
    wall_ground_location(line_9, 360, "5", wall_vertical_picture)
    wall_ground_location(line_10, 400, "5", wall_vertical_picture)
    wall_ground_location(line_11, 440, "5", wall_vertical_picture)
    wall_ground_location(line_12, 480, "5", wall_vertical_picture)
    wall_ground_location(line_13, 520, "5", wall_vertical_picture)
    wall_ground_location(line_14, 560, "5", wall_vertical_picture)

    wall_ground_location(line_0, 0, "6", ground_picture)
    wall_ground_location(line_1, 40, "6", ground_picture)
    wall_ground_location(line_2, 80, "6", ground_picture)
    wall_ground_location(line_3, 120, "6", ground_picture)
    wall_ground_location(line_4, 160, "6", ground_picture)
    wall_ground_location(line_5, 200, "6", ground_picture)
    wall_ground_location(line_6, 240, "6", ground_picture)
    wall_ground_location(line_7, 280, "6", ground_picture)
    wall_ground_location(line_8, 320, "6", ground_picture)
    wall_ground_location(line_9, 360, "6", ground_picture)
    wall_ground_location(line_10, 400, "6", ground_picture)
    wall_ground_location(line_11, 440, "6", ground_picture)
    wall_ground_location(line_12, 480, "6", ground_picture)
    wall_ground_location(line_13, 520, "6", ground_picture)
    wall_ground_location(line_14, 560, "6", ground_picture)
    
    return
    
        







        






