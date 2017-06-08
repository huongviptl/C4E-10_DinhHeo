import pygame

from sokoban_rebuild import Game
from game_object.box import Box
from game_object.dest import Dest
from game_object.map import Map
from game_object.pusher import Pusher


sokoban = Game()
sokoban.map = Map(5, 5)
sokoban.pusher = Pusher(1, 1)
sokoban.box = Box(2, 2)
sokoban.dest = Dest(3, 3)
sokoban.console_draw()

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
box_image = pygame.image.load("images/box.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")
win_image = pygame.image.load("images/victory.jpg")

sokoban.box.image = box_image
sokoban.dest.image = dest_image
sokoban.pusher.image = pusher_image

pixel = 64

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        sokoban.handle_input(event)

    if sokoban.check_win():
        sokoban.dest.image = pygame.image.load("images/victory.jpg")
        sokoban.draw(screen, ground_image)
        done = True

    sokoban.draw(screen, ground_image)
    pygame.display.flip()
