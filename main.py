#  this file was created by your nameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee

# importing libraryyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
'''PowerUp 2 player self destruct laser projectiles phasing buffs scenery godemode different villains









'''



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
        pg.display.set_caption(" WHY U PLAY THIS ")
        #tracks time using ticksnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500,100)
        self.running= True
        #later store info
        # run method- responsible for running gameeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
        self.load_data()
    def load_data(self):
        game_folder = path.dirname(__file__)
        # img_folder = path.join(game_folder, "images")
        # self.player_img = pg.image.load(path.join(img_folder, 'sleim.png')).convert_alpha()
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
        print("new game waiting to be beat...")
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.mobs = pg.sprite.Group()
        self.power_ups = pg.sprite.Group()
       # self.player = Player(self,10,10)
       # self.all_sprites.add(self.player)
        #for x in range(10,20):
         #Wall(self,x,5)
        for row, tiles in enumerate(self.map_data):
            print(row)
            for col, tile in enumerate(tiles):
                print(col)
                if tile == '1':
                    print("a wall at", row, col)
                    Wall(self, col, row)
                if tile == 'P':
                    self.player = Player(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'U':
                    PowerUp(self, col, row)
                if tile == 'P2':
                    self.player2 = Player2(self, col, row)
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
                
    def draw_text(self, surface, text, size, color, x, y):
        font_name = pg.font.match_font('comic_sans')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x,y)
        surface.blit(text_surface, text_rect)
        
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.player.moneybag), 64, WHITE, 1, 1)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
                print("GAME OVER")
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