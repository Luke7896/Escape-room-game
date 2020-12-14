"""
Program: Settings.py
Author: Lucas Forcier

Defines constant variables in one place 
so they can be easily found and changed
all on one page.
"""

#imports pygame and random
import pygame as pg
import random


# defines colors
WHITE = (255, 255, 255)
DARKGREY = (40, 40, 40)

# game settings
WIDTH = 1024  
HEIGHT = 768  
FPS = 60
TITLE = "ESCAPE"
BGCOLOR = DARKGREY
FONT_NAME = 'arial'
TILESIZE = 32
#GRIDWIDTH = WIDTH / TILESIZE
#GRIDHEIGHT = HEIGHT / TILESIZE
MUSIC1 = 'tune.wav'
MUSIC2 = 'tune2.wav'
MUSIC_LIST = [MUSIC1, MUSIC2]
SUCCESS_SOUND = 'success.wav'
LOCKED = 'locked.wav'
FAIL = 'fail.wav'
display_dict = {1:"You find nothing interesting", 
                2:"The door is locked!",
                3:"You Win!",
                4:"You found the orange disc!",
                5:"You found the blue disc!",
                6:"You found the yellow disc!"}

# player settings
PLAYER_IMG = 'manBlue_hold2.png'

# map settings
# walls
WALL_VERT = 'wall_vertical2.png'
WALL_CORNER = 'wall_corner1.png'
WALL_CONNECT = 'connectwall.png'

# room object images
TV = 'tv.png'
COUNTER = 'counter.png'
STOVE = 'stove.png'
SINK = 'sink.png'
CHAIR = 'chair.png'
BIG_PLANT = 'plant1.png'
BIG_BOX = 'box.png'
SMALL_BOX = 'box2.png'
DOOR = 'door.png'
TV_LEFT = 'tv_left.png'
TV_RIGHT = 'tv_right.png'
COUCH_L = 'couch_left.png'
COUCH_M = 'couch_middle.png'
COUCH_R = 'couch_right.png'
TABLE = 'table.png'

# decoration object images
SMALL_PLANT = 'plant2.png'
SPLATTER = 'splatter.png'
STICK = 'stick.png'
PLANK = 'plank.png'

# Goals
O_DISC = 'orange.png'
B_DISC = 'blue.png'
Y_DISC = 'yellow.png'

