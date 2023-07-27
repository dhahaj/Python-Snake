import pygame

class GameView:
    def __init__(self, game, screen):
        self.game = game
        self.screen = screen

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.game.snake.draw(self.screen)
        self.game.food.draw(self.screen)
        pygame.display.update()
