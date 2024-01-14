import pygame
from FacillimumLibrary import Facillimum_Library
from marioAnimation import Mario
from settings import Settings

class Coins:
  def __init__(self, ai_game) -> None:
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.image = pygame.image.load('images/coin.png')
    self.image = pygame.transform.scale(self.image, (75, 60))
    self.rect = self.image.get_rect()
    self.revealer = pygame.image.load('images/coin_revealer.png')
    self.revealer_rect = self.revealer.get_rect()
    self.FL = Facillimum_Library(self.screen)
    self.mario = Mario(self)
    self.settings = Settings()
    self.move_right = False
    self.move_left = False
    
  def draw_coins(self):
    self.FL.draw_image(self.image, (0, 0))
    self.FL.draw_image(self.image, (75, 0))
    self.FL.draw_image(self.image, (150, 0))
    self.FL.draw_image(self.image, (225, 0))
    self.FL.draw_image(self.image, (300, 0))
    self.FL.draw_image(self.image, (375, 0))
    self.FL.draw_image(self.image, (450, 0))
    self.FL.draw_image(self.image, (525, 0))
    self.FL.draw_image(self.image, (600, 0))
    self.FL.draw_image(self.image, (675, 0))

  def reveal_coins(self):
    self.revealer_rect.x += 75

  def reset_x(self):
    self.revealer_rect.x = 0

  def blitme(self):
    self.screen.blit(self.revealer, self.revealer_rect)