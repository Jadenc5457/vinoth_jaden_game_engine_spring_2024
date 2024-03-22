#this file was created by chris brad field who copied it from Notch/Jaden Vinoth
#write a wall class

from turtle import Vec2D
import pygame as pg
from settings import *
from random import choice

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image = game.player_img
        #self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 300
        self.moneybag = 0
        self.status= ""
        self.pos = (0,0)
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -self.speed
            print(self.rect.x)
            print(self.rect.y)
        if keys[pg.K_RIGHT]:
            self.vx = self.speed
        if keys[pg.K_UP]:
            self.vy = -self.speed
        if keys[pg.K_DOWN]:
            self.vy = self.speed


    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
#thanks aayush
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
            if str(hits[0].__class__.__name__) == "PowerUp":
                self.speed += player_speed

    # def get_keys(self):
    #     self.vx, self.vy = 0, 0
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_LEFT] or keys[pg.K_a]:
    #         self.vx = -player_speed
    #         print(self.rect.x)
    #         print(self.rect.y)
    #     if keys[pg.K_RIGHT] or keys[pg.K_d]:
    #         self.vx = player_speed
    #     if keys[pg.K_UP] or keys[pg.K_w]:
    #         self.vy = player_speed
    #     if keys[pg.K_DOWN] or keys[pg.K_s]:
    #     if self.vx != 0 and self.vy != 0:
    #         self.vx *= 0.7071
    #         self.vy *= 0.7071

    

    


    # def speedpotion(self, ):
    #     hits = pg.sprite.spritecollide(self,self.game.speedpotion, False)
    #     if hits:
    #         #increase speed
    #         self.speed 

        # self.x+=dx
        # self.x+=dy

   
        # self.rect.x = self.x
        # self.rect.y = self.y
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        # add collision
        self.collide_with_walls('x')
        self.rect.y = self.y
        # add collision
        self.collide_with_walls('y')
        self.collide_with_group(self.game.coins, True)
        self.collide_with_group(self.game.power_ups, True)
        # self.rect.x = self.x * TILESIZE
        # self.rect.y = self.y * TILESIZE

# coin_hits = pg.sprite.spritecollide(self.game.coins, True)
        # if coin_hits:
        #     print("I got a coin")

   
    #     self.vx, self.vy = 0, 0
    #     self.x = x * TILESIZE
    #     self.y = y * TILESIZE
    #     self.moneybag = 0

    # def get_keys(self):
    #     self.vx, self.vy = 0, 0
    # def collide_with_walls(self, dir):
    #             self.y = hits[0].rect.bottom
    #             self.vy = 0
    #             self.rect.y = self.y


    # def collide_with_group(self, group, kill):
    #     hits = pg.sprite.spritecollide(self, group, kill)
    #     if hits:
    #         if str(hits[0].__class__.__name__) == "Coin":
    #             self.moneybag += 1

    # def update(self):
    #     self.get_keys()
    # def update(self):
    #     self.rect.y = self.y
    #     # add collision later
    #     self.collide_with_walls('y')
    #     self.collide_with_group(self.game.coins, True)

        # coin_hits = pg.sprite.spritecollide(self.game.coins, True)
        # if coin_hits:
        #     print("I got a coin")



#player 2 code is basically a copy from player 1
class Player2(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        # self.image = pg.Surface((TILESIZE, TILESIZE))
        # self.image.fill(RED)
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 300
        self.moneybag = 0
        self.status= ""
        self.pos = (0,0)
    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()   
        if keys[pg.K_a]:
            self.vx = -self.speed
        if keys[pg.K_d]:
            self.vx = self.speed
        if keys[pg.K_w]:
            self.vy = -self.speed
        if keys[pg.K_s]:
            self.vy = self.speed          
            print(self.rect.x)
            print(self.rect.y)
    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y
    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            if str(hits[0].__class__.__name__) == "Coin":
                self.moneybag += 1
            if str(hits[0].__class__.__name__) == "PowerUp":
                self.speed += player_speed
    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        # add collision
        self.collide_with_walls('x')
        self.rect.y = self.y
        # add collision
        self.collide_with_walls('y')
        self.collide_with_group(self.game.coins, True)
        self.collide_with_group(self.game.power_ups, True)



class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGRAY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
    # def update(self):
    #     # self.rect.x += 1
    #     self.rect.x += TILESIZE * self.speed
    #     # self.rect.y += TILESIZE * self.speed
    #     if self.rect.x > width or self.rect.x < 0:
    #         self.speed *= -1
        # if self.rect.y > HEIGHT or self.rect.y < 0:
        #     self.speed *= -1
class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        
class PowerUp(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.power_ups
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.speed = 1
    # def collide_with_walls(self, dir):
    #     if dir == 'x':
    #         print('colliding on the x')
    #         hits = pg.sprite.spritecollide(self, self.game.walls, False)
    #         if hits:
    #             if self.vx > 0:
    #                 self.x = hits[0].rect.left - self.rect.width
    #             if self.vx > 0:
    #                 self.x = hits[0].rect.right
    #             self.vx = 0
    #             self.rect.x = self.x
    #     if dir == 'y':
    #         print('colliding on the y')
    #         hits = pg.sprite.spritecollide(self, self.game.walls, False)
    #         if hits:
    #            if self.vy > 0:
    #             self.y - hits[0].rect.top - self.rect.height
    #             if self.vy < 0:
    #                 self.y = hits[0].rect.bottom
    #             self.vy = 0
    #             self.rect.y = self.y
    def update(self):
        # self.rect.x += 1
        self.rect.x += TILESIZE * self.speed
        # self.rect.y += TILESIZE * self.speed
        if self.rect.x > width or self.rect.x < 0:
            self.speed *= -1
        # if self.rect.y > HEIGHT or self.rect.y < 0:
        #     self.speed *= -1
        # # self.rect.x += 1
        # self.x += self.vx * self.game.dt
        # self.y += self.vy * self.game.dt
        
        # if self.rect.x < self.game.player.rect.x:
        #     self.vx = 100
        # if self.rect.x > self.game.player.rect.x:
        #     self.vx = -100    
        # if self.rect.y < self.game.player.rect.y:
        #     self.vy = 100
        # if self.rect.y > self.game.player.rect.y:
        #     self.vy = -100
        # self.rect.x = self.x
        # self.collide_with_walls('x')
        # self.rect.y = self.y
        # self.collide_with_walls('y')



# class speedpotion(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game. speedpotion
#         pg.sprite.Sprite.__init__(self,self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE,TILESIZE))
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE
#         self.speed = 0


# class enemy(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites, game.walls
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill(RED)
#         self.rect = self.image.get_rect()
#         self.x = x
#         self.y = y
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE
#         self.speed = 4
#     def update(self):
#          self.rect.x += TILESIZE
#          self.rect.y += TILESIZE
#          if self.rect.x > width:
#              self.rect.x