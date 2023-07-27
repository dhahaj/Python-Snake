import pygame
from model import Game
from view import GameView
from controller import GameController

SCREEN_WIDTH = 480
SCREEN_HEIGHT = 480
GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT // GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH // GRIDSIZE
UP = (0,-1)
DOWN = (0,1)
LEFT = (-1,0)
RIGHT = (1,0)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    game = Game()
    game_view = GameView(game, screen)
    game_controller = GameController(game)

    while True:
        for event in pygame.event.get():
            game_controller.handle_event(event)

        game.update()
        game_view.draw()
        pygame.display.update()
        clock.tick(12)

if __name__ == "__main__":
    main()
