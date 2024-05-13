#this file was created by chris brad field who copied it from Notch/Jaden Vinoth
#write a wall class
from typing import Self
import pygame
import math
from turtle import Vec2D
from utils import*
import pygame as pg
from settings import *
from random import choice
from os import path
import images
# sword_image = pygame.image.load('sword.png')
rot = 7

vec =pg.math.Vector2
SPRITESHEET = "sleim.png"

game_folder = path.dirname(__file__)
img_folder = path.join(game_folder, 'images')





# class Spritesheet:
    
#     # utility class for loading and parsing spritesheets
#     def __init__(self, filename):
#         self.spritesheet = pg.image.load(filename).convert()

#     def get_image(self, x, y, width, height):
#         # grab an image out of a larger spritesheet
#         image = pg.Surface((width, height))
#         image.blit(self.spritesheet, (0, 0), (x, y, width, height))
#         # image = pg.transform.scale(image, (width, height))
#         image = pg.transform.scale(image, (width * 1, height * 1))
#         return image

# class Sword(pg.sprite.Sprite):
#     def __init__(self, game, x, y):
#         self.groups = game.all_sprites
#         pg.sprite.Sprite.__init__(self, self.groups)
#         self.game = game
#         self.image = pg.Surface((TILESIZE, TILESIZE))
#         self.image.fill((255, 255, 0))  # Yellow color (you can change this)
#         self.rect = self.image.get_rect()
#         self.rect.x = x * TILESIZE
#         self.rect.y = y * TILESIZE

    # def update(self):
    #     # Check for collision with the player
    #     hits = pg.sprite.spritecollide(self, self.game.players, False)
    #     if hits:
    #         # Handle ollision with the player
    #         player = hits[0]
    #         player.pick_up_sword(self)
    #         self.kill()
class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, name, health=100):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.name = name
        self.health = health
        self.inventory = []
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.vx, self.vy = 0, 0
        self.speed = 300
        self.moneybag = 0
        self.status = ""
        self.pos = (0, 0)

    def pick_up_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

    def display_inventory(self):
        print(f"{self.name}'s inventory:")
        if self.inventory:
            for item in self.inventory:
                print(item)
        else:
            print("Inventory is empty.")

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} takes {damage} damage. Health: {self.health}")

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -self.speed
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
                    self.rect.right = hits[0].rect.left
                if self.vx < 0:
                    self.rect.left = hits[0].rect.right
                self.vx = 0
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.rect.bottom = hits[0].rect.top
                if self.vy < 0:
                    self.rect.top = hits[0].rect.bottom
                self.vy = 0

    def collide_with_group(self, group, kill):
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            for hit in hits:
                if isinstance(hit, Coin):
                    self.moneybag += 1
                elif isinstance(hit, PowerUp):
                    self.speed += player_speed

    def update(self, group, kill):
        self.player.update(self.coins, True)
        hits = pg.sprite.spritecollide(self, group, kill)
        if hits:
            self.get_keys()
        self.rect.x += self.vx * self.game.dt
        self.collide_with_walls('x')
        self.rect.y += self.vy * self.game.dt
        self.collide_with_walls('y')
        self.collide_with_group(self.game.coins, True)
        self.collide_with_group(self.game.power_ups, True)
        self.collide_with_group(self.game.Sword, False)
        if str(hits[0].__class__.__name__) == "Sword":
                print("you found a sword")
                hits[0].attached = True
class Game:
    
    def __init__(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, 0, 0, "Player")

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
        #hey this is the way the players move
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
            #how we do not go through walls
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
                #how we are able to touch coins and collect them
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


#class or what this wall is
class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        # self.image.fill(LIGHTGRAY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
class Wallc(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        # self.image.fill(LIGHTGRAY)
        # self.rect = self.image.get_rect()
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
        #ooh shiny coin
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
        #speedy thingy
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
class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def update_position(self):
        # Move projectile according to its direction
        pass

    def check_collision(self, mob):
        # Check collision with mob
        if self.x == mob.x and self.y == mob.y:
            mob.kill()
#Does not work right when placed but still working on it
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        # self.image = self.game.mob_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vx, self.vy = 100, 100
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.speed = 300
        self.health = 32
        self.max_health = 32

        print("created mob at", self.rect.x, self.rect.y)
    def collide_with_walls(self, dir):
        if dir == 'x':
            # print('colliding on the x')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vx *= -1
                self.rect.x = self.x
        if dir == 'y':
            # print('colliding on the y')
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                self.vy *= -1
                self.rect.y = self.y
    def chasing(self):
        if self.rect.x < self.game.player.rect.x:
            self.vx = 100
        if self.rect.x > self.game.player.rect.x:
            self.vx = -100    
        if self.rect.y < self.game.player.rect.y:
            self.vy = 100
        if self.rect.y > self.game.player.rect.y:
            self.vy = -100
  
    def draw_health(self):
        # calculate health ratio
        health_ratio = self.health / self.max_health
        # calculate width of health bar
        health_width = int(self.rect.width * health_ratio)
        # create health bar
        health_bar = pg.Rect(0, 0, health_width, 7)
        # position health bar
        health_bar.midtop = self.rect.midtop
        # draw health bar
        pg.draw.rect(self.image, GREEN, health_bar)
    # def draw_health(self):
    #     if self.hitpoints > 31:
    #         col = GREEN
    #     elif self.hitpoints > 15:
    #         col = YELLOW
    #     else:
    #         col = RED
    #     width = int(self.rect.width * self.hitpoints / MOB_HITPOINTS)
    #     self.health_bar = pg.Rect(0, 0, width, 7)
    #     if self.hitpoints < MOB_HITPOINTS:
    #         pg.draw.rect(self.image, col, self.health_bar)

    
    def update(self):
        if self.health < 1:
            self.kill()
        # self.image.blit(self.game.screen, self.pic)
        # pass
        # # self.rect.x += 1
        # self.chasing()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')
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


#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.alive = True

#     def kill(self):
#         self.alive = False
#         print("Mob killed!")

# # Example usage:
# if __name__ == "__main__":
#     player = Player(0, 0)
#     player.shoot("right")

#     mob = Mob(1, 0)

#     for projectile in player.projectiles:
#         projectile.check_collision(mob)
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

class Enemy:
    def __init__(self, target):
        self.x = width // 2
        self.y = height // 2
        self.target = target
        self.image = BLACK
    

    def move_towards(self):
        dx = self.target.x - self.x
        dy = self.target.y - self.y
        dist = math.sqrt(dx ** 2 + dy ** 2)
        if dist != 0:
            dx = dx / dist
            dy = dy / dist
            self.x += dx
            self.y += dy

    def check_collision(self, mob):
        if pygame.Rect(self.x, self.y, self.rect.width, self.rect.height).colliderect(mob.rect):
            return True
        return False

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# class shield(pg.sprite.Sprite):


class sword(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.sword
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BGCOLOR)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.attached = False
    def attach(self, player):
        self.rect.x = player.rect.x + 16
        self.rect.y = player.rect.y + 16
        self.x = player.rect.x + 16
        self.y = player.rect.y + 16
    def update(self):
        if self.attached:
            self.attach(self.game.player)
        self.rect.x = self.x
        self.rect.y = self.y
# class Item:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

# # Initialize Pygame
# pg.init()
# #modified from chat gpt for picking up items
# # Example usage:
# game = Game()

# player = Player(game, 0, 0, "Player",) 
# item2 = Item("Shield")
# item1 = Item("Sword")  

# player.pick_up_item(item1)  # Pass the 'item1' instance as an argument to the pick_up_item() method

# player.pick_up_item(item2)

# player.display_inventory()


# Main loop
running = True