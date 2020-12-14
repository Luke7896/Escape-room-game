



import pygame as pg
from settings import *
import math

class Player(pg.sprite.Sprite):
    """Defines the player class"""
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.middle = self.rect.center
        self.x = x
        self.y = y
        

    def move(self, dx=0, dy=0):
        """Adds dx or dy to player's x or y value"""
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        """Checks if a movement would collide player with a wall"""
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False


    def interact_distance(self, rect1x, rect2x, rect1y, rect2y):
        """Determines if player is within interation range of an object"""
        dist = math.sqrt((rect2x - rect1x) ** 2 + (rect2y - rect1y) ** 2)
        if dist >= 1.3:
            return False
        else:
            return True

    def update(self):
        """Updates the player class"""
        self.events()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    def events(self):
        """Maps keyboard controls for the player"""
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.type == pg.QUIT:
                    pg.display.quit()
                    self.game.quit()
                    self.game.sys.exit()
                if event.key == pg.K_ESCAPE:
                    pg.display.quit()
                    self.game.quit()
                    self.game.sys.exit()
                if event.key == pg.K_LEFT:
                    self.move(dx=-1)
                    self.image = self.game.player_img_l
                if event.key == pg.K_RIGHT:
                    self.move(dx=1)
                    self.image = self.game.player_img
                if event.key == pg.K_UP:
                    self.move(dy=-1)
                    self.image = self.game.player_img_u
                if event.key == pg.K_DOWN:
                    self.move(dy=1) 
                    self.image = self.game.player_img_d
                if event.key == pg.K_SPACE:
                    self.search()
    
    def search(self):
        """Interacts with an object if within range of it"""
        if self.interact_distance(self.x, self.game.secret_box.x, self.y, self.game.secret_box.y):
            if self.game.found_b == False:
                self.game.status = display_dict[5]
                self.game.found_b = True
                pg.mixer.Sound.play(self.game.success)
        elif self.interact_distance(self.x, self.game.secret_plant.x, self.y, self.game.secret_plant.y):
            if self.game.found_y == False:
                self.game.status = display_dict[6]
                self.game.found_y = True
                pg.mixer.Sound.play(self.game.success)
        elif self.interact_distance(self.x, self.game.secret_couch.x, self.y, self.game.secret_couch.y):
            if self.game.found_o == False:
                self.game.status = display_dict[4]
                self.game.found_o = True
                pg.mixer.Sound.play(self.game.success)
        elif self.interact_distance(self.x, self.game.secret_door.x, self.y, self.game.secret_door.y):
            if self.game.found_b == True:
                if self.game.found_y == True:
                    if self.game.found_o == True:
                        self.game.status = display_dict[3]
                        self.game.game_over = True
            else:
                self.game.status = display_dict[2]
                pg.mixer.Sound.play(self.game.locked)
        else:
            self.game.status = display_dict[1]
            pg.mixer.Sound.play(self.game.fail)
                    

class Wall(pg.sprite.Sprite):
    """Defines the wall class"""
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Decor(pg.sprite.Sprite):
    """Defines the decor class"""
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Hidden(pg.sprite.Sprite):
    """Defines the hidden object class"""
    def __init__(self, game, x, y, image):
        self.groups = game.all_sprites, game.walls, game.hidden
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = image
        self.rect = self.image.get_rect()
        self.middle = self.rect.center
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


