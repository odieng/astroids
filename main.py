import pygame as pg
from constants import *
from player import Player
def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock =  pg.time.Clock()
    dt = 0

    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill((0, 0, 0))
        player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
        player.draw(screen)
        pg.display.flip()
        dt = clock.tick(60)/1000.0

if __name__ == "__main__":
    main()