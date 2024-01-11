import pygame

class Mario:
  def __init__(self, ai_game) -> None:
    self.screen = ai_game.screen
    self.screen_rect = ai_game.screen.get_rect()
    self.image = pygame.image.load('images/mario_standing.png')
    self.image = pygame.transform.scale(self.image, (75, 60))
    self.jumping_image = pygame.image.load('images/mario_jumping.png')
    self.jumping_image = pygame.transform.scale(self.jumping_image, (75, 60))
    self.falling_image = pygame.image.load('images/mario_falling.png')
    self.falling_image = pygame.transform.scale(self.falling_image, (75, 60))
    self.rect = self.image.get_rect()
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    self.jump = False
    self.fall = False
    self.animate = False
    self.x = 610
    self.y = 554
    self.rect.x = self.x
    self.rect.y = self.y
    self.time = 0

  def animate_jump(self):
    self.image = self.jumping_image
    self.rect.y = 350

  def animate_lose(self):
    self.image = self.falling_image

  def blitme(self):
    self.screen.blit(self.image, self.rect)
    