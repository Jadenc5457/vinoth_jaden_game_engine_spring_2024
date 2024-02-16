#  this file was created by your nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# importing libraryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
import pygame as pg
from settings import *
from Sprites import *
from random import randint
import sys
from os import path


#creating game class now or elseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

class Game:
    #initialize class
    def __init__(self):
        pg.init()
        #pygame.init()))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))
        #setting dimensions for varaiables imported from settingseeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        self.screen = pg.display.set_mode((width,height))
        #create captionnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        pg.display.set_caption(" no ending ")
        #tracks time using ticksnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.running= True
        #later store info
        # run method- responsible for running gameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        self.map_data = []
        '''
        The with statement is a context manager in Python. 
        It is used to ensure that a resource is properly closed or released 
        after it is used. This can help to prevent errors and leaks.
        '''
        with open(path.join(game_folder, 'map.txt'),'rt' ) as f:
            #goes through lines and puts it into list
            for line in f:
                print(line)
                self.map_data.append(line)
                print(self.map_data)
        #for making new game
    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
       # self.player = Player(self,10,10)
       # self.all_sprites.add(self.player)
        #for x in range(10,20):
         #Wall(self,x,5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall is here supposedly", row, col)
                    Wall(self, col, row)
                # if tile == '3':
                #     print ("ohh scary", row ,col)
                #     enemy(self,col, row)
                if tile== 'p':
                    self.player = Player(self, col, row)
            
                if tile== 'z':
                    self.player = Player(self, col, row)
            
                # if tile == 'z':
                #     self.player = speedpotion(self, col, row)
    def run(self):
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS)/1000
            self.events()
            #input
            self.update()
            #process
            self.draw()
            #output

        #will not run only on thissssssssssssssssssssssssssssssssssssssssssssssssssssssssssss


    def quit(self):
        pg.quit()
        sys.exit()
        #methods
    def input(self):    
        pass
    def update(self):
        self.all_sprites.update()

    def draw_grid(self):
        for x in range(0,width,TILESIZE):
            pg.draw.line(self.screen,LIGHTGRAY,(x, 0),(x,height))
        for y in range(0, height, TILESIZE):
            pg.draw.line(self.screen, LIGHTGRAY,(0, y), (width ,y))
                
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
    def events(self):
            for event in pg.event.get():
                # when you hit the red x the window closes the game ends
                if event.type == pg.QUIT:
                    self.quit()
                    print("GAME OVER!!")
                    print("TOO BAD SUCKER!!!")
                    print("GET BETTER NOOB")
                #keybinds
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_LEFT:
                #         self.player.move(dx=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_RIGHT:
                #         self.player.move(dx=1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_UP:
                #         self.player.move(dy=-1)
                # if event.type == pg.KEYDOWN:
                #     if event.key == pg.K_DOWN:
                #         self.player.move(dy=1)
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass
#assigns the Game to the variableeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
g = Game()
#g.show_go_screen()
while True:
    g.new()
    g.run()
    #g.show_go_screen()