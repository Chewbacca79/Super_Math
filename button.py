import pygame
from FacillimumLibrary import Facillimum_Library

class Button:
  def __init__(self, ai_game) -> None:
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.image = pygame.image.load('images/Play_again_button.png')
    self.rect = self.image.get_rect()
    self.FL = Facillimum_Library(self.screen)
    self.button_pressed = False

  def display_button(self):
    self.FL.draw_image(self.image, (400, 400))
    if pygame.mouse.get_pos[0] > 400 and pygame.mouse.get_pos[0] < 500:
      if pygame.mouse.get_pos[1] > 400 and pygame.mouse.get_pos[1] < 462 and pygame.mouse.get_pressed(3) == (True, False, False):
        self.button_pressed = True
        print("ding")
      