"""
"""

import pygame as pg 
import sys
import random
from os import path
from settings import *
from sprites import *

class Game:
    """Defines the game object"""
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.font_name = pg.font.match_font(FONT_NAME)
        pg.key.set_repeat(500, 100)
        self.load_data()
      

    def load_data(self):
        """Loads all the data needed for the game"""
        # defines game and image folders
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'img')
        sound_folder = path.join(game_folder, 'music')
        # loads map.txt file and puts it in a list
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)
        # load sounds
        self.song = random.choice(MUSIC_LIST)
        self.music1 = pg.mixer.music.load(path.join(sound_folder, self.song))
        self.success = pg.mixer.Sound(path.join(sound_folder, SUCCESS_SOUND))
        self.locked = pg.mixer.Sound(path.join(sound_folder, LOCKED))
        self.fail = pg.mixer.Sound(path.join(sound_folder, FAIL))
        # loads images
        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
        self.player_img_l = pg.transform.flip(self.player_img, True, False).convert_alpha()
        self.player_img_u = pg.transform.rotate(self.player_img, 90)
        self.player_img_d = pg.transform.rotate(self.player_img, 270)
        self.wall_vert = pg.image.load(path.join(img_folder, WALL_VERT)).convert_alpha()
        self.wall_hori = pg.transform.rotate(self.wall_vert, 90)
        self.wall_corner_tr = pg.image.load(path.join(img_folder, WALL_CORNER)).convert_alpha()
        self.wall_corner_tl = pg.transform.rotate(self.wall_corner_tr, 90)
        self.wall_corner_bl = pg.transform.rotate(self.wall_corner_tr, 180)
        self.wall_corner_br = pg.transform.rotate(self.wall_corner_tr, 270)
        self.wall_connect_lr = pg.image.load(path.join(img_folder, WALL_CONNECT)).convert_alpha()
        self.wall_connect_bu = pg.transform.rotate(self.wall_connect_lr, 90)
        self.wall_connect_rl = pg.transform.rotate(self.wall_connect_lr, 180)
        self.wall_connect_ub = pg.transform.rotate(self.wall_connect_lr, 270)
        self.sink = pg.image.load(path.join(img_folder, SINK)).convert_alpha()
        self.counter = pg.image.load(path.join(img_folder, COUNTER)).convert_alpha()
        self.stove = pg.image.load(path.join(img_folder, STOVE)).convert_alpha()
        self.tv = pg.image.load(path.join(img_folder, TV)).convert_alpha()
        self.chair = pg.image.load(path.join(img_folder, CHAIR)).convert_alpha()
        self.chair2 = pg.transform.rotate(self.chair, 180)
        self.big_box = pg.image.load(path.join(img_folder, BIG_BOX)).convert_alpha()
        self.big_box2 = pg.transform.flip(self.big_box, True, False)
        self.plant = pg.image.load(path.join(img_folder, BIG_PLANT)).convert_alpha()
        self.plank = pg.image.load(path.join(img_folder, PLANK)).convert_alpha()
        self.plank2 = pg.transform.rotate(self.plank, 90)
        self.splatter = pg.image.load(path.join(img_folder, SPLATTER)).convert_alpha()
        self.stick = pg.image.load(path.join(img_folder, STICK)).convert_alpha()
        self.y_disc = pg.image.load(path.join(img_folder, Y_DISC)).convert_alpha()
        self.o_disc = pg.image.load(path.join(img_folder, O_DISC)).convert_alpha()
        self.b_disc = pg.image.load(path.join(img_folder, B_DISC)).convert_alpha()
        self.couch_m = pg.image.load(path.join(img_folder, COUCH_M)).convert_alpha()
        self.couch_l = pg.image.load(path.join(img_folder, COUCH_L)).convert_alpha()
        self.couch_r = pg.image.load(path.join(img_folder, COUCH_R)).convert_alpha()
        self.couch_vm = pg.transform.rotate(self.couch_m, 90)
        self.couch_ll = pg.transform.rotate(self.couch_l, 90)
        self.couch_lr = pg.transform.rotate(self.couch_r, 90)
        self.tv_l = pg.image.load(path.join(img_folder, TV_LEFT)).convert_alpha()
        self.tv_r = pg.image.load(path.join(img_folder, TV_RIGHT)).convert_alpha()
        self.tv_left = pg.transform.flip(self.tv_l, False, True)
        self.tv_right = pg.transform.flip(self.tv_r, False, True)
        self.door = pg.image.load(path.join(img_folder, DOOR)).convert_alpha()

    def new(self):
        """Initializes game variables and sets up a new game"""
        # Creates sprite groups
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.hidden = pg.sprite.Group()
        # Game variables
        self.found_b = False
        self.found_o = False
        self.found_y = False
        self.status = ""
        self.game_over = False
        # creates game map from .txt file
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, self.wall_hori)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'v':
                    Wall(self, col, row, self.wall_vert)
                if tile == 'c':
                    Wall(self, col, row, self.wall_corner_tr)
                if tile == 'z':
                    Wall(self, col, row, self.wall_corner_bl)
                if tile == 'x':
                    Wall(self, col, row, self.wall_corner_br)
                if tile == 'a':
                    Wall(self, col, row, self.wall_corner_tl)
                if tile == 's':
                    Wall(self, col, row, self.wall_connect_bu)
                if tile == 'd':
                    Wall(self, col, row, self.wall_connect_rl)
                if tile == 'f':
                    Wall(self, col, row, self.wall_connect_lr)
                if tile == 'i':
                    Wall(self, col, row, self.wall_connect_ub)
                if tile == 'g':
                    Wall(self, col, row, self.sink)
                if tile == 'h':
                    Wall(self, col, row, self.counter)
                if tile == 'j':
                    Wall(self, col, row, self.stove)
                if tile == 'k':
                    Wall(self, col, row, self.tv)
                if tile == 'l':
                    Wall(self, col , row, self.chair2)
                if tile == 'q':
                    Wall(self, col, row, self.big_box)
                if tile == 'w':
                    Wall(self, col, row, self.big_box2)
                if tile == 'e':
                    Wall(self, col, row, self.plant)
                if tile == 'r':
                    Decor(self, col, row, self.plank)
                if tile == 'o':
                    Decor(self, col, row, self.plank2)
                if tile == 't':
                    Decor(self, col, row, self.splatter)
                if tile == 'y':
                    Decor(self, col, row, self.stick)
                if tile == '9':
                    self.secret_box = Hidden(self, col, row, self.big_box2)
                if tile == '8':
                    self.secret_plant = Hidden(self, col, row, self.plant)
                if tile == '7':
                    self.secret_couch = Hidden(self, col, row, self.couch_r)
                if tile == '6':
                    Wall(self, col, row, self.couch_l)
                if tile == '5':
                    Wall(self, col, row, self.couch_r)
                if tile == '4':
                    Wall(self, col, row, self.tv_left)
                if tile == '3':
                    Wall(self, col, row, self.tv_right)
                if tile == '!':
                    Wall(self, col, row, self.couch_vm)
                if tile == '@':
                    Wall(self, col, row, self.couch_ll)
                if tile == '#':
                    Wall(self, col, row, self.couch_lr)
                if tile == '%':
                    self.secret_door = Hidden(self, col, row, self.door)
                    
                
    def run(self):
        """Runs the main game loop"""
        self.playing = True
        while self.playing:
            # Shows the game over screen if the game is over
            if self.game_over == True:
                self.game_over_screen()
                self.new()
            else:
                self.dt = self.clock.tick(FPS) / 1000
                self.update()
                self.draw()

    def quit(self):
        """Closes the game window"""
        pg.display.quit()
        sys.exit()

    def update(self):
        """Updates all of the sprites"""
        self.all_sprites.update()

    def draw(self):
        """Draws sprites, text, and information to the screen"""
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_text("Status", 22, WHITE, WIDTH / 4, 8)
        self.draw_text(str(self.status), 22, WHITE, WIDTH / 4, 32)
        self.draw_text("Inventory", 22, WHITE, 800, 8)
        if self.found_b == True:
            self.screen.blit(self.b_disc, (750, 32))
        if self.found_o == True:
            self.screen.blit(self.o_disc, (800, 32))
        if self.found_y == True:
            self.screen.blit(self.y_disc, (850, 32))
        pg.display.flip() 
                   
    def draw_text(self, text, size, color, x, y):
        """ draws text to screen """
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def wait_for_key(self):
        """Holds game at a screen until key is pressed"""
        # creates a new queue of button presses
        pg.event.wait()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                    self.quit()
                if event.type == pg.KEYUP:
                    waiting = False

    def start_screen(self):
        """Displays information when you start the game"""
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 90, WHITE, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Press any key to continue", 32, WHITE, WIDTH / 2, HEIGHT * 3/4)
        self.draw_text("Press arrow keys to move. Spacebar to search for objects.", 32, 
                                                WHITE, WIDTH / 2, HEIGHT / 2)
        pg.display.flip()
        self.wait_for_key()

    def game_over_screen(self):
        """Shows information after game is over"""
        self.screen.fill(BGCOLOR)
        self.draw_text("YOU WIN!", 90, WHITE, WIDTH / 2, HEIGHT * 1/4)
        self.draw_text("Press any key to start a new game", 32, WHITE, WIDTH / 2, HEIGHT * 3/4)
        pg.display.flip()
        self.wait_for_key()
        self.game_over = False

# create the game object
g = Game()
#initialize start screen
g.start_screen()

# Starts game loop
while True:
        g.new()
        pg.mixer.music.play(-1)
        pg.mixer.music.set_volume(0.2)
        g.run()
        