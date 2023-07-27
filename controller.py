import pygame

class GameController:
    def __init__(self, game):
        self.game = game

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.game.snake.turn(UP)
            elif event.key == pygame.K_DOWN:
                self.game.snake.turn(DOWN)
            elif event.key == pygame.K_LEFT:
                self.game.snake.turn(LEFT)
            elif event.key == pygame.K_RIGHT:
                self.game.snake.turn(RIGHT)
